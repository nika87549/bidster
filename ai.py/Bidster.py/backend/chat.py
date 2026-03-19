from flask import Blueprint, request, jsonify
from datetime import datetime

chat_bp = Blueprint("chat", __name__)

MESSAGES = []  # დროებითი მეხსიერება

@chat_bp.route("/send", methods=["POST"])
def send_message():
    data = request.json
    user_id = data.get("user_id")
    auction_id = data.get("auction_id")
    text = data.get("text")

    if not text:
        return jsonify({"error": "Empty message"}), 400

    message = {
        "user_id": user_id,
        "auction_id": auction_id,
        "text": text,
        "timestamp": datetime.utcnow().isoformat()
    }

    MESSAGES.append(message)
    return jsonify({"message": "sent"})


@chat_bp.route("/get/<int:auction_id>", methods=["GET"])
def get_messages(auction_id):
    msgs = [m for m in MESSAGES if m["auction_id"] == auction_id]
    return jsonify(msgs)



from flask_socketio import emit, join_room
from app import socketio

@socketio.on("join_room")
def handle_join(data):
    room = data["auction_id"]
    join_room(room)

@socketio.on("send_message")
def handle_message(data):
    auction_id = data["auction_id"]
    emit("new_message", data, room=auction_id)