from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class Customer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    account_number: str
    balance: Decimal
