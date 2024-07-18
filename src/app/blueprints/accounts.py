from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.database import db
from app.helpers import handle_errors
from app.models import Account
from app.schemas.accounts import AccountDTO

bp = Blueprint("Accounts", __name__, url_prefix="/")


@bp.get("/conta")
def get_account():
    account_number = request.args.get("numero_conta", "")
    account = (
        db.session.query(Account)
        .where(Account.account_number == account_number)
        .first()
    )
    if account is None:
        return jsonify({"error": "account not found"}), 404
    return (
        jsonify({"numero_conta": account.account_number, "saldo": account.balance}),
        200,
    )


@bp.post("/conta")
def create_account():
    data = request.get_json()
    try:
        # validate payload
        account_dto = AccountDTO(
            account_number=data["numero_conta"], balance=data["saldo"]
        )
        with current_app.app_context():
            # fill account object
            account = Account(
                account_number=account_dto.account_number, balance=account_dto.balance
            )
            # save in database
            db.session.add(account)
            db.session.commit()
            db.session.refresh(account)

        return (
            jsonify({"numero_conta": account.account_number, "saldo": account.balance}),
            201,
        )
    except ValidationError as e:
        errors = handle_errors(e.errors())
        return jsonify(errors), 401
