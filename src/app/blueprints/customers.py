from flask import Blueprint, jsonify, request

bp = Blueprint("customers", __name__, url_prefix="/")

@bp.post("/conta")
def create_account():
    data = request.get_json()
    account_number = data["numero_conta"]
    balance = data["saldo"]
    response = {"conta":{"numero_conta": account_number, "saldo": balance}}
    return jsonify(response)
