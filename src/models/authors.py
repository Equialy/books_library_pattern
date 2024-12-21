from datetime import date

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.authors import AuthorsSchema


class Authors(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    second_name: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[date] = mapped_column(nullable=False)

    def to_read_model(self) -> AuthorsSchema:
        return AuthorsSchema(
            id=self.id,
            name=self.name,
            second_name=self.second_name,
            birthday=self.birthday
        )