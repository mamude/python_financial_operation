from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import db


class Account(db.Model):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_number: Mapped[String] = mapped_column(String(50))
    balance: Mapped[Numeric] = mapped_column(Numeric(precision=10, scale=2))

    # foreignkey configuration
    transactions: Mapped[list["Transaction"]] = db.relationship(
        "Transaction", back_populates="account"
    )


class Transaction(db.Model):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    payment_method: Mapped[String] = mapped_column(String(1))
    value: Mapped[Numeric] = mapped_column(Numeric(precision=10, scale=2))
    balance_history: Mapped[Numeric] = mapped_column(Numeric(precision=10, scale=2))

    # foreignkey configuration
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    account: Mapped["Account"] = db.relationship(
        "Account", back_populates="transactions"
    )
