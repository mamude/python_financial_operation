from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.database import db
from app.helpers import handle_errors
from app.models import Account
from app.schemas.accounts import AccountDTO

bp = Blueprint("Accounts", __name__, url_prefix="/")


@bp.post("/conta")
def create_account():
    data = request.get_json()
    try:
        # validate data
        account_dto = AccountDTO(
            account_number=data["numero_conta"], balance=data["saldo"]
        )
        with current_app.app_context():
            # fill Account object
            account = Account(
                account_number=account_dto.account_number, balance=account_dto.balance
            )
            # save in database
            db.session.add(account)
            db.session.commit()

        return jsonify(account_dto.model_dump()), 201
    except ValidationError as e:
        errors = handle_errors(e.errors())
        return jsonify(errors), 401
