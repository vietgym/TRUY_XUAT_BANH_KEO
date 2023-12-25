"""initial user

Revision ID: 9d5a8bf96952
Revises: 1ef2b30b6223
Create Date: 2023-12-21 21:05:54.724893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d5a8bf96952'
down_revision: Union[str, None] = '1ef2b30b6223'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("userID", sa.String, primary_key=True, index=True),
        sa.Column("userName", sa.String),
        sa.Column("userEmail", sa.String),
        sa.Column("userLg", sa.String),
        sa.Column("userPass", sa.String),
        sa.Column("role", sa.String),
    )


def downgrade() -> None:
    op.drop_table("users")