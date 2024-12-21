from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped,mapped_column
from src.db.db import Base
from src.schemas.books import  BookSchema




class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    describe: Mapped[str] = mapped_column(nullable=False)
    id_author: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="quantity_non_negative"),
    )

    def to_read_model(self) -> BookSchema:
        return BookSchema(
            id=self.id,
            title=self.title,
            describe=self.describe,
            id_author=self.id_author,
            quantity=self.quantity
        )
