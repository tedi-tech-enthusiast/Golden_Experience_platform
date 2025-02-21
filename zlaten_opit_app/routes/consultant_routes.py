from flask import Blueprint, request, jsonify
import db

consultant_bp = Blueprint("consultant", __name__)

# 📌 GET - Извличане на всички консултанти
@consultant_bp.route("/consultants", methods=["GET"])
def get_all_consultants():
    consultants = db.db_query("SELECT * FROM consultants")
    return jsonify(consultants)

# 📌 GET - Извличане на един консултант по ID
@consultant_bp.route("/consultants/<int:consultant_id>", methods=["GET"])
def get_consultant(consultant_id):
    consultant = db.db_query(f"SELECT * FROM consultants WHERE id = {consultant_id}")
    return jsonify(consultant)

# 📌 POST - Създаване на нов консултант
@consultant_bp.route("/consultants", methods=["POST"])
def create_consultant():
    data = request.get_json()
    name = data.get("name")
    experience = data.get("experience")
    skills = data.get("skills")

    query = f"INSERT INTO consultants (name, experience, skills) VALUES ('{name}', '{experience}', '{skills}')"
    db.db_insert(query)

    return jsonify({"message": "Consultant added successfully!"}), 201

# 📌 PUT - Обновяване на консултант по ID
@consultant_bp.route("/consultants/<int:consultant_id>", methods=["PUT"])
def update_consultant(consultant_id):
    data = request.get_json()
    name = data.get("name")
    experience = data.get("experience")
    skills = data.get("skills")

    query = f"UPDATE consultants SET name='{name}', experience='{experience}', skills='{skills}' WHERE id={consultant_id}"
    db.db_insert(query)

    return jsonify({"message": "Consultant updated successfully!"})

# 📌 DELETE - Изтриване на консултант по ID
@consultant_bp.route("/consultants/<int:consultant_id>", methods=["DELETE"])
def delete_consultant(consultant_id):
    query = f"DELETE FROM consultants WHERE id={consultant_id}"
    db.db_insert(query)

    return jsonify({"message": "Consultant deleted successfully!"})
