from flask import Blueprint, jsonify
from auth import USERS
from auction import AUCTIONS, BIDS, TICKETS

stats_bp = Blueprint("stats", __name__)


# 1) აქტიური მომხმარებლები (ვინც ბოლო 24 საათში იყო აქტიური)
@stats_bp.route("/active_users", methods=["GET"])
def active_users():
    active = len(USERS)  # მოგვიანებით დავამატებთ რეალურ აქტივობას
    return jsonify({"active_users": active})


# 2) ქვეყნების მიხედვით დათვლა
@stats_bp.route("/countries", methods=["GET"])
def countries():
    country_count = {}
    for u in USERS:
        c = u["country"]
        country_count[c] = country_count.get(c, 0) + 1
    return jsonify(country_count)


# 3) გამარჯვებულების რაოდენობა
@stats_bp.route("/winners", methods=["GET"])
def winners():
    winners = [a for a in AUCTIONS if a["winner_user_id"] is not None]
    return jsonify({"total_winners": len(winners)})


# 4) მონაწილეობების რაოდენობა (რამდენ აუქციონში მიიღო მონაწილეობა)
@stats_bp.route("/participation", methods=["GET"])
def participation():
    participation_count = {}

    for t in TICKETS:
        uid = t["user_id"]
        participation_count[uid] = participation_count.get(uid, 0) + 1

    return jsonify(participation_count)


# 5) ბიდების რაოდენობა თითოეულ აუქციონზე
@stats_bp.route("/bids_per_auction", methods=["GET"])
def bids_per_auction():
    result = {}
    for a in AUCTIONS:
        count = len([b for b in BIDS if b["auction_id"] == a["id"]])
        result[a["title"]] = count
    return jsonify(result)