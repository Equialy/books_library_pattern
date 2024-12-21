from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.models.books import Books
from src.utils.base import BaseRepository
from src.utils.repository import SQLAlchemyRepository


class BooksRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Books)

    # async def get_one_by_id(self, id: int) -> Books:
    #     stmt = select(self.model).where(self.model.id == id)
    #     result = await self.session.execute(stmt)
    #     return result.scalar_one()

    async def add_one(self, data: dict) -> Books:
        item = self.model(**data)
        self.session.add(item)
        try:
            await self.session.flush()
        except IntegrityError:
            raise HTTPException(status_code=400,
                                detail="Нарушение ограничения внешнего ключа: id_author отсутствует в таблице authors.")
        return item

    # async def find_all(self) -> list[Books]:
    #     stmt = select(self.model)
    #     result = await self.session.execute(stmt)
    #     result = [row[0].to_read_model() for row in result.all()]
    #     return result

    async def delete_one(self, data_id):
        stmt = delete(self.model).where(self.model.id == data_id).returning(self.model)
        result = await self.session.execute(stmt)
        try:
            return result.scalar_one()
        except NoResultFound:
            raise HTTPException(status_code=400, detail=f"Запись не найдена")
