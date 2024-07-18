from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict


class PaymentMethod(str, Enum):
    Pix = "P"
    CreditCard = "C"
    DebitCard = "D"


class TransactionDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    payment_method: PaymentMethod
    account_number: str
    value: Decimal
