from flask import Blueprint, request, jsonify
import db
from models.user import User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users_data = db.db_query("SELECT id, name, email, user_type FROM users")
    users = [User(*data).to_dict() for data in users_data]
    return jsonify(users)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    db.db_insert("INSERT INTO users (name, email, user_type) VALUES (%s, %s, %s)",
                 (data["name"], data["email"], data["user_type"]))
    return jsonify({"message": "User created successfully"}), 201
