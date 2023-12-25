"""initial

Revision ID: 1ef2b30b6223
Revises: 
Create Date: 2023-12-21 20:58:03.672341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ef2b30b6223'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("proID", sa.String, primary_key=True, index=True),
        sa.Column("proName", sa.String),
        sa.Column("manufacturerAdd", sa.String),
        sa.Column("manufacturerName", sa.String),
        sa.Column("manufacturerCont", sa.String),
        sa.Column("distributorAdd", sa.String),
        sa.Column("distributorName", sa.String),
        sa.Column("distributorCont", sa.String),
        sa.Column("otherDetails", sa.String),
    )


def downgrade() -> None:
    op.drop_table("products")
