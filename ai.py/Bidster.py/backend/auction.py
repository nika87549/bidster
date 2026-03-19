from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta

auction_bp = Blueprint("auction", __name__)

# დროებითი მონაცემები (მოგვიანებით DB-ს დავუკავშირებთ)
AUCTIONS = []
TICKETS = []
BIDS = []
TICKET_ID = 1
BID_ID = 1


# ბილეთის ყიდვა
@auction_bp.route("/buy_ticket", methods=["POST"])
def buy_ticket():
    global TICKET_ID

    data = request.json
    user_id = data.get("user_id")
    auction_id = data.get("auction_id")

    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    if auction["status"] != "active" and auction["status"] != "scheduled":
        return jsonify({"error": "Auction is not open"}), 400

    # ბილეთის შექმნა
    ticket = {
        "id": TICKET_ID,
        "user_id": user_id,
        "auction_id": auction_id,
        "bids_left": auction["max_bids_per_ticket"],
        "created_at": datetime.utcnow()
    }

    TICKETS.append(ticket)
    TICKET_ID += 1

    auction["total_tickets_sold"] += 1

    return jsonify({"message": "Ticket purchased", "ticket_id": ticket["id"]})


# ბიდის გაკეთება
@auction_bp.route("/bid", methods=["POST"])
def place_bid():
    global BID_ID

    data = request.json
    user_id = data.get("user_id")
    auction_id = data.get("auction_id")

    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    if auction["status"] != "active":
        return jsonify({"error": "Auction is not active"}), 400

    # მოძებნე ბილეთი
    ticket = next((t for t in TICKETS if t["user_id"] == user_id and t["auction_id"] == auction_id and t["bids_left"] > 0), None)
    if not ticket:
        return jsonify({"error": "No bids left"}), 400

    # დროის ლიმიტის შემოწმება
    now = datetime.utcnow()
    last_bid = next((b for b in reversed(BIDS) if b["auction_id"] == auction_id), None)

    if last_bid:
        diff = (now - last_bid["created_at"]).total_seconds()
        if diff > auction["bid_timeout_seconds"]:
            # აუქციონი დასრულდა
            auction["status"] = "finished"
            auction["winner_user_id"] = last_bid["user_id"]
            auction["winner_price"] = last_bid["amount"]
            return jsonify({"message": "Auction finished", "winner": last_bid["user_id"]})

    # ბიდის გაკეთება
    bid = {
        "id": BID_ID,
        "user_id": user_id,
        "auction_id": auction_id,
        "amount": auction["start_price"] + len([b for b in BIDS if b["auction_id"] == auction_id]) * 1,
        "created_at": now,
        "is_last_active": True
    }

    # წინა ბიდი აღარ არის აქტიური
    for b in BIDS:
        if b["auction_id"] == auction_id:
            b["is_last_active"] = False

    BIDS.append(bid)
    BID_ID += 1

    # ბილეთის ბიდების შემცირება
    ticket["bids_left"] -= 1

    return jsonify({"message": "Bid placed", "bid_id": bid["id"], "amount": bid["amount"]})



from flask import jsonify

@auction_bp.route("/status/<int:auction_id>", methods=["GET"])
def auction_status(auction_id):
    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    now = datetime.utcnow()
    remaining_seconds = int((auction["end_datetime"] - now).total_seconds())
    if remaining_seconds < 0:
        remaining_seconds = 0

    last_bid = next((b for b in reversed(BIDS) if b["auction_id"] == auction_id), None)

    return jsonify({
        "status": auction["status"],
        "remaining_seconds": remaining_seconds,
        "last_bidder_id": last_bid["user_id"] if last_bid else None,
        "last_bid_amount": last_bid["amount"] if last_bid else None
    })