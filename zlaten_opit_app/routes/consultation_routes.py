from flask import Blueprint, request, jsonify
import db

consultation_bp = Blueprint("consultation", __name__)

# 📌 GET - Вземи всички консултации
@consultation_bp.route("/consultations", methods=["GET"])
def get_all_consultations():
    consultations = db.db_query("SELECT * FROM consultations")
    return jsonify(consultations)

# 📌 GET - Вземи конкретна консултация по ID
@consultation_bp.route("/consultations/<int:consultation_id>", methods=["GET"])
def get_consultation(consultation_id):
    consultation = db.db_query(f"SELECT * FROM consultations WHERE id = {consultation_id}")
    return jsonify(consultation)

# 📌 POST - Създай нова консултация
@consultation_bp.route("/consultations", methods=["POST"])
def create_consultation():
    data = request.get_json()
    consultant_id = data.get("consultant_id")
    client_id = data.get("client_id")
    details = data.get("details")

    query = f"INSERT INTO consultations (consultant_id, client_id, details) VALUES ({consultant_id}, {client_id}, '{details}')"
    db.db_insert(query)

    return jsonify({"message": "Consultation created successfully!"}), 201

# 📌 DELETE - Изтрий консултация по ID
@consultation_bp.route("/consultations/<int:consultation_id>", methods=["DELETE"])
def delete_consultation(consultation_id):
    query = f"DELETE FROM consultations WHERE id={consultation_id}"
    db.db_insert(query)

    return jsonify({"message": "Consultation deleted successfully!"})
