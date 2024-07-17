from flask import Blueprint, abort, jsonify, request
from pydantic import ValidationError

from app.schemas.customers import Customer as SchemaCustomer

bp = Blueprint("customers", __name__, url_prefix="/")

@bp.post("/conta")
def create_account():
    data = request.get_json()
    try:
        # validate data send
        customer = SchemaCustomer(account_number=data["numero_conta"], balance=data["saldo"])
        return jsonify(customer.model_dump())
    except ValidationError as e:
        abort(401, jsonify(e.errors()))
    return jsonify(False)
