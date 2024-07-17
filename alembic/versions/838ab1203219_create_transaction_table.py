"""create transaction table

Revision ID: 838ab1203219
Revises: 36dc5033d082
Create Date: 2024-07-17 13:05:33.034844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '838ab1203219'
down_revision: Union[str, None] = '36dc5033d082'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("account_id", sa.Integer, nullable=False),
        sa.Column("payment_method", sa.String(1), nullable=False),
        sa.Column("value", sa.DECIMAL(2), nullable=False),
        sa.Column("balance", sa.DECIMAL(2), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default="now()"),
        # foreign key
        sa.ForeignKeyConstraint(["account_id"], ["accounts.id"], onupdate="CASCADE", ondelete="CASCADE")
    )


def downgrade() -> None:
    op.drop_table("transactions")
