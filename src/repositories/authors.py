from sqlalchemy import insert, select, delete

from src.models.authors import Authors
from src.utils.base import BaseRepository
from src.utils.repository import SQLAlchemyRepository


class AuthorRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Authors)

    # async def get_one_by_id(self, id: int) -> Authors:
    #     stmt = select(self.model).where(self.model.id == id)
    #     result = await self.session.execute(stmt)
    #     return result.scalar_one()


    async def add_one(self, data: dict) -> Authors:
        item = self.model(**data)
        self.session.add(item)
        await self.session.flush()
        return item
        # stmt = insert(self.model).values(**data).returning(self.model)
        # result = await self.session.execute(stmt)
        # return result.scalar_one()

    # async def find_all(self):
    #     stmt = select(self.model)
    #     result = await self.session.execute(stmt)
    #     result = [row[0].to_read_model() for row in result.all()]
    #     return result

    async def delete_one(self, data_id: dict):
        stmt = delete(self.model).where(self.model.id == data_id["id"]).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()


