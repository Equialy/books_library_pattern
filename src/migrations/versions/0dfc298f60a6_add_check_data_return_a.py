"""Add check data return a

Revision ID: 0dfc298f60a6
Revises: 7096e421c753
Create Date: 2024-12-21 21:16:29.539973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0dfc298f60a6'
down_revision: Union[str, None] = '7096e421c753'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        constraint_name="check_data_return",
        table_name="borrows",
        condition="date_return IS NULL OR date_return >= date_borrow"
    )


def downgrade() -> None:
    op.drop_constraint(
        constraint_name="check_data_return",
        table_name="borrows",
        type_="check"
    )
