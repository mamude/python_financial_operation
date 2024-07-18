from dataclasses import dataclass

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import db


@dataclass
class Account(db.Model):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_number: Mapped[String] = mapped_column(String(50))
    balance: Mapped[Numeric] = mapped_column(Numeric(precision=10, scale=2))
