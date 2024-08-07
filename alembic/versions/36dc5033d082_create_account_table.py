"""create account table

Revision ID: 36dc5033d082
Revises:
Create Date: 2024-07-17 12:44:05.472481

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '36dc5033d082'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "accounts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("account_number", sa.String(50), nullable=False, unique=True),
        sa.Column("balance", sa.DECIMAL(precision=10, scale=2), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("accounts")
