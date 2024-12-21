"""Add check constraint for quantity in books table

Revision ID: 935c6afa645a
Revises: 3196d4b95ceb
Create Date: 2024-12-21 20:38:01.044966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '935c6afa645a'
down_revision: Union[str, None] = '3196d4b95ceb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        "quantity_non_negative",  # Имя ограничения
        "books",  # Имя таблицы
        "quantity >= 0"  # Условие проверки
    )


def downgrade() -> None:
    op.drop_constraint(
        "quantity_non_negative",  # Имя ограничения
        "books",  # Имя таблицы
        type_="check"  # Тип ограничения
    )