from decimal import Decimal

from pydantic import BaseModel, ConfigDict, field_validator
from sqlalchemy import select

from app.database import db
from app.models import Account


class AccountDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    account_number: str
    balance: Decimal

    @field_validator("account_number")
    @classmethod
    def account_number_must_be_unique(cls, value: str) -> str:
        q = db.session.query(Account).filter(Account.account_number == value).exists()
        if q := db.session.scalar(select(q)):
            raise ValueError("this account already exists")
        return value
