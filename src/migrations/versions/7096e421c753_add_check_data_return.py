"""Add check data return

Revision ID: 7096e421c753
Revises: a6115040beb1
Create Date: 2024-12-21 21:08:19.387464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7096e421c753'
down_revision: Union[str, None] = 'a6115040beb1'
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
