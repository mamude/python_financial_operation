from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.database import db
from app.helpers import handle_errors
from app.models import Account, Transaction
from app.schemas.transactions import TransactionDTO

bp = Blueprint("Transactions", __name__, url_prefix="/")


@bp.post("/transacao")
def create_transaction():
    data = request.get_json()
    try:
        # validate payload
        transaction_dto = TransactionDTO(
            payment_method=data["forma_pagamento"],
            account_number=data["numero_conta"],
            value=data["valor"],
        )
        with current_app.app_context():
            # fill transaction object
            transaction = Transaction(
                payment_method=transaction_dto.payment_method,
                value=transaction_dto.value,
                balance_history=transaction_dto.balance,
                account_id=transaction_dto.account_id,
            )
            db.session.add(transaction)
            db.session.commit()

        return jsonify(transaction_dto.model_dump()), 201
    except ValidationError as e:
        errors = handle_errors(e.errors())
        return jsonify(errors), 401
