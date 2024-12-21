"""Add check

Revision ID: a6115040beb1
Revises: 935c6afa645a
Create Date: 2024-12-21 20:41:53.643663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6115040beb1'
down_revision: Union[str, None] = '935c6afa645a'
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