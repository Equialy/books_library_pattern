from os import times_result

from sqlalchemy import select, delete, update, insert

from src.models.books import Books
from src.models.borrows import Borrows
from src.schemas.borrows import BorrowSchema, BorrowSchemaAdd, BorrowsSchemaReturn
from src.utils.base import BaseRepository
from src.utils.repository import SQLAlchemyRepository


class BorrowsRepository(BaseRepository):

    def __init__(self, session):
        super().__init__(session, Borrows)
    # async def get_one_by_id(self, id: int) -> Borrows:
    #     stmt = select(self.model).where(self.model.id == id)
    #     result = await self.session.execute(stmt)
    #     try:
    #         return result.scalar_one()
    #     except:
    #         raise HTTPException(status_code=400, detail="Запись выдачи не найдена.")


    # async def find_all(self) -> list[Borrows]:
    #     stmt = select(self.model)
    #     result = await self.session.execute(stmt)
    #     result = [row[0].to_read_model() for row in result.all()]
    #     return result

    async def add_one(self, data: BorrowSchemaAdd) -> Borrows:
        query_add_borrow = insert(self.model).values(data.model_dump()).returning(self.model)
        query_update_book = update(Books).where(Books.id == data.id_book).values(quantity=Books.quantity - 1)
        result_add = await self.session.execute(query_add_borrow)
        await self.session.execute(query_update_book)

        return result_add.scalar_one()


    async def delete_one(self, data_id: int) -> Borrows:
        stmt = delete(self.model).where(self.model.id == data_id).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def return_borrows(self, borrow_id: int, date_return: BorrowsSchemaReturn) -> Borrows:
        query_update_borrow = update(self.model).where(self.model.id == borrow_id).where(self.model.date_return.is_(None)).values(date_return=date_return.date_return).returning(self.model)
        query_update_book = update(Books).where(Books.id == date_return.id_book).values(quantity=Books.quantity + 1)
        result_borrow = await self.session.execute(query_update_borrow)
        await self.session.execute(query_update_book)
        return result_borrow.scalar_one()
