from flask import Blueprint, request, jsonify
import os

profile_bp = Blueprint("profile", __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

from auth import USERS

@profile_bp.route("/upload_avatar/<int:user_id>", methods=["POST"])
def upload_avatar(user_id):
    if "avatar" not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files["avatar"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    ext = file.filename.rsplit(".", 1)[-1].lower()
    filename = f"user_{user_id}.{ext}"
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    user = next((u for u in USERS if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user["avatar_url"] = f"/uploads/{filename}"

    return jsonify({"message": "Avatar uploaded", "avatar_url": user["avatar_url"]})