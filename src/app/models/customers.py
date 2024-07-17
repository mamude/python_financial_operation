from dataclasses import dataclass
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.database import db

@dataclass
class Customers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    account_number: Mapped[String]
    balance: Mapped[Numeric]

