from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
import datetime

bcrypt = Bcrypt()
auth = Blueprint("auth", __name__)

SECRET_KEY = "CHANGE_THIS_TO_A_LONG_RANDOM_KEY"

# დრო JWT-სთვის
TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 საათი

# დროებითი users list (მოგვიანებით DB-ს დავუკავშირებთ)
USERS = []
USER_ID_COUNTER = 1


def create_jwt(user_id, email, is_admin):
    payload = {
        "user_id": user_id,
        "email": email,
        "is_admin": is_admin,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


@auth.route("/register", methods=["POST"])
def register():
    global USER_ID_COUNTER

    data = request.json
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    address = data.get("address")
    country = data.get("country")

    # Email duplication check
    if any(u["email"] == email for u in USERS):
        return jsonify({"error": "Email already exists"}), 400

    pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    user = {
        "id": USER_ID_COUNTER,
        "email": email,
        "password_hash": pw_hash,
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "country": country,
        "is_admin": False,
        "total_bids": 0,
        "total_auctions_participated": 0,
        "total_wins": 0
    }

    USERS.append(user)
    USER_ID_COUNTER += 1

    return jsonify({"message": "Registered successfully"})


@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = next((u for u in USERS if u["email"] == email), None)

    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    if not bcrypt.check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Invalid email or password"}), 401

    token = create_jwt(user["id"], user["email"], user["is_admin"])

    return jsonify({"message": "Login successful", "token": token})