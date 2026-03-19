# from flask import Blueprint, request, jsonify
# from datetime import datetime
# from auction import AUCTIONS

# admin_bp = Blueprint("admin", __name__)

# # დროებითი admin user check (მოგვიანებით JWT-დან ამოვიღებთ)
# ADMIN_IDS = [1]  # user_id = 1 არის admin


# def is_admin(user_id):
#     return user_id in ADMIN_IDS


# # ახალი აუქციონის შექმნა
# @admin_bp.route("/create_auction", methods=["POST"])
# def create_auction():
#     data = request.json
#     user_id = data.get("user_id")

#     if not is_admin(user_id):
#         return jsonify({"error": "Unauthorized"}), 403

#     auction = {
#         "id": len(AUCTIONS) + 1,
#         "title": data["title"],
#         "description": data["description"],
#         "image_url": data["image_url"],
#         "start_price": data["start_price"],
#         "ticket_price": data["ticket_price"],
#         "max_bids_per_ticket": data["max_bids_per_ticket"],
#         "start_datetime": datetime.fromisoformat(data["start_datetime"]),
#         "end_datetime": datetime.fromisoformat(data["end_datetime"]),
#         "bid_timeout_seconds": data["bid_timeout_seconds"],
#         "total_tickets_available": data["total_tickets_available"],
#         "total_tickets_sold": 0,
#         "status": "scheduled",
#         "winner_user_id": None,
#         "winner_price": None,
#         "winner_message_text": ""
#     }

#     AUCTIONS.append(auction)

#     return jsonify({"message": "Auction created", "auction_id": auction["id"]})


# # აუქციონის წაშლა
# @admin_bp.route("/delete_auction", methods=["POST"])
# def delete_auction():
#     data = request.json
#     user_id = data.get("user_id")
#     auction_id = data.get("auction_id")

#     if not is_admin(user_id):
#         return jsonify({"error": "Unauthorized"}), 403

#     for a in AUCTIONS:
#         if a["id"] == auction_id:
#             AUCTIONS.remove(a)
#             return jsonify({"message": "Auction deleted"})

#     return jsonify({"error": "Auction not found"}), 404


# # აუქციონის რედაქტირება
# @admin_bp.route("/edit_auction", methods=["POST"])
# def edit_auction():
#     data = request.json
#     user_id = data.get("user_id")
#     auction_id = data.get("auction_id")

#     if not is_admin(user_id):
#         return jsonify({"error": "Unauthorized"}), 403

#     auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
#     if not auction:
#         return jsonify({"error": "Auction not found"}), 404

#     # განახლება
#     for key in data:
#         if key in auction and key != "id":
#             auction[key] = data[key]

#     return jsonify({"message": "Auction updated"})


# # გამარჯვებულის ტექსტის მითითება
# @admin_bp.route("/set_winner_message", methods=["POST"])
# def set_winner_message():
#     data = request.json
#     user_id = data.get("user_id")
#     auction_id = data.get("auction_id")
#     message = data.get("message")

#     if not is_admin(user_id):
#         return jsonify({"error": "Unauthorized"}), 403

#     auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)
#     if not auction:
#         return jsonify({"error": "Auction not found"}), 404

#     auction["winner_message_text"] = message

#     return jsonify({"message": "Winner message updated"})




from flask import Blueprint, request, jsonify
from datetime import datetime
from auction import AUCTIONS

admin_bp = Blueprint("admin", __name__)

# დროებითი admin user check
ADMIN_IDS = [1]  # user_id = 1 არის admin

def is_admin(user_id):
    return user_id in ADMIN_IDS


# ახალი აუქციონის შექმნა
@admin_bp.route("/create", methods=["POST"])
def create_auction():
    data = request.json
    user_id = data.get("user_id", 1)  # დროებით admin

    if not is_admin(user_id):
        return jsonify({"error": "Unauthorized"}), 403

    auction = {
        "id": len(AUCTIONS) + 1,
        "title": data["title"],
        "description": data["description"],
        "image_url": data["image_url"],
        "start_price": data["start_price"],
        "ticket_price": data["ticket_price"],
        "max_bids_per_ticket": data["max_bids_per_ticket"],
        "start_datetime": datetime.fromisoformat(data["start_datetime"]),
        "end_datetime": datetime.fromisoformat(data["end_datetime"]),
        "bid_timeout_seconds": data["bid_timeout_seconds"],
        "total_tickets_available": data["total_tickets_available"],
        "total_tickets_sold": 0,
        "status": "scheduled",
        "winner_user_id": None,
        "winner_price": None,
        "winner_message_text": ""
    }

    AUCTIONS.append(auction)

    return jsonify({"message": "Auction created", "auction_id": auction["id"]})


# აუქციონის წაშლა
@admin_bp.route("/delete/<int:auction_id>", methods=["DELETE"])
def delete_auction(auction_id):
    global AUCTIONS
    AUCTIONS = [a for a in AUCTIONS if a["id"] != auction_id]
    return jsonify({"message": "Auction deleted"})


# აუქციონის რედაქტირება
@admin_bp.route("/edit/<int:auction_id>", methods=["PUT"])
def edit_auction(auction_id):
    data = request.json
    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)

    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    for key in data:
        if key in auction:
            auction[key] = data[key]

    return jsonify({"message": "Auction updated"})


# გამარჯვებულის ტექსტის მითითება
@admin_bp.route("/winner_message/<int:auction_id>", methods=["PUT"])
def set_winner_message(auction_id):
    data = request.json
    message = data.get("winner_message")

    auction = next((a for a in AUCTIONS if a["id"] == auction_id), None)

    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    auction["winner_message_text"] = message

    return jsonify({"message": "Winner message updated"})