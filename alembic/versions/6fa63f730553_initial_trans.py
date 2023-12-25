"""initial trans

Revision ID: 6fa63f730553
Revises: 9d5a8bf96952
Create Date: 2023-12-21 21:38:06.818301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fa63f730553'
down_revision: Union[str, None] = '9d5a8bf96952'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "trans",
        sa.Column("transID", sa.String, primary_key=True, index=True),
        sa.Column("transTime", sa.String),
        sa.Column("transHash", sa.String),
        sa.Column("userID", sa.String, sa.ForeignKey("users.userID", ondelete="CASCADE")),
        sa.Column("productID", sa.String, sa.ForeignKey("products.proID", ondelete="CASCADE")),
    )


def downgrade() -> None:
    op.drop_table("trans")
