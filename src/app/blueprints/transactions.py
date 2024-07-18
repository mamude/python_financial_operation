from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.database import db
from app.helpers import handle_errors
from app.schemas.transactions import TransactionDTO

bp = Blueprint("Transactions", __name__, url_prefix="/")


@bp.post("/transacao")
def create_transaction():
    data = request.get_json()
    try:
        transaction_dto = TransactionDTO(
            payment_method=data["forma_pagamento"],
            account_number=data["numero_conta"],
            value=data["valor"],
        )
        return jsonify(transaction_dto.model_dump()), 201
    except ValidationError as e:
        errors = handle_errors(e.errors())
        return jsonify(errors), 401
