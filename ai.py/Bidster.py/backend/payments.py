from flask import Blueprint, request, jsonify
import stripe
import uuid

payments_bp = Blueprint("payments", __name__)

# Stripe Secret Key (შემდეგ შეცვლი რეალურზე)
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

# დროებითი ბილეთების სია (მოგვიანებით DB-ს დავუკავშირებთ)
from auction import TICKETS, TICKET_ID, AUCTIONS


# Stripe გადახდის შექმნა
@payments_bp.route("/stripe/create_payment", methods=["POST"])
def create_stripe_payment():
    data = request.json
    user_id = data.get("user_id")
    auction_id = data.get("auction_id")

    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    amount = int(auction["ticket_price"] * 100)  # Stripe იღებს თეთრებში

    # უნიკალური გადახდის ID
    payment_id = str(uuid.uuid4())

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": f"Bidster Ticket for {auction['title']}"},
                "unit_amount": amount
            },
            "quantity": 1
        }],
        mode="payment",
        success_url="http://localhost:5000/payment_success?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://localhost:5000/payment_cancel",
        metadata={"user_id": user_id, "auction_id": auction_id, "payment_id": payment_id}
    )

    return jsonify({"checkout_url": session.url})


# Stripe Webhook — გადახდის დადასტურება
@payments_bp.route("/stripe/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = "YOUR_STRIPE_WEBHOOK_SECRET"

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except Exception:
        return "Invalid signature", 400

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        user_id = int(session["metadata"]["user_id"])
        auction_id = int(session["metadata"]["auction_id"])

        global TICKET_ID

        # ბილეთის ჩაწერა
        ticket = {
            "id": TICKET_ID,
            "user_id": user_id,
            "auction_id": auction_id,
            "bids_left": next(a for a in AUCTIONS if a["id"] == auction_id)["max_bids_per_ticket"]
        }

        TICKETS.append(ticket)
        TICKET_ID += 1

    return "OK", 200












from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

# PayPal კონფიგურაცია (Sandbox გასატესტად)
PAYPAL_CLIENT_ID = "YOUR_PAYPAL_CLIENT_ID"
PAYPAL_CLIENT_SECRET = "YOUR_PAYPAL_SECRET"

environment = SandboxEnvironment(client_id=PAYPAL_CLIENT_ID, client_secret=PAYPAL_CLIENT_SECRET)
paypal_client = PayPalHttpClient(environment)


@payments_bp.route("/paypal/create_payment", methods=["POST"])
def create_paypal_payment():
    data = request.json
    user_id = data.get("user_id")
    auction_id = data.get("auction_id")

    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    amount = str(auction["ticket_price"])

    request_order = OrdersCreateRequest()
    request_order.prefer("return=representation")
    request_order.request_body({
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": amount
            }
        }],
        "application_context": {
            "return_url": "http://localhost:5000/paypal_success",
            "cancel_url": "http://localhost:5000/paypal_cancel"
        }
    })

    response = paypal_client.execute(request_order)
    approve_link = next(link.href for link in response.result.links if link.rel == "approve")

    return jsonify({"approve_url": approve_link})
