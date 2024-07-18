from decimal import Decimal
from enum import Enum
from typing import Optional, Self

from pydantic import BaseModel, ConfigDict, model_validator

from app.database import db
from app.models import Account


class PaymentMethod(str, Enum):
    Pix = "P"
    CreditCard = "C"
    DebitCard = "D"


class Taxes(Decimal, Enum):
    TaxCreditCard = 0.50
    TaxDebitCard = 0.30


class TransactionDTO(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, use_enum_values=True, arbitrary_types_allowed=True
    )

    payment_method: PaymentMethod
    account_number: str
    value: Decimal
    balance: Optional[Decimal] = None
    account_id: Optional[int] = None

    @model_validator(mode="after")
    def account_must_exists(self) -> Self:
        account = (
            db.session.query(Account)
            .where(Account.account_number == self.account_number)
            .first()
        )
        # check if account exists
        if account is None:
            raise ValueError("account not found")

        # check payment method and make calculation
        payment_method = PaymentMethod(self.payment_method)
        if payment_method.value == "D":
            account.balance = (account.balance - self.value) - Taxes.TaxDebitCard
        if payment_method.value == "C":
            account.balance = (account.balance - self.value) - Taxes.TaxCreditCard
        if payment_method.value == "P":
            account.balance = account.balance - self.value

        # check if account has balance positive
        if account.balance < 0:
            raise ValueError("account has no balance")

        # update dto object
        self.balance = account.balance
        # set account id
        self.account_id = account.id
        # update balance account
        db.session.commit()
