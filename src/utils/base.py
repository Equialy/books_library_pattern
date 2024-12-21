from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.repository import SQLAlchemyRepository


class BaseRepository(SQLAlchemyRepository):

    def __init__(self, session: AsyncSession, model):
        super().__init__(session)
        self.model = model

    async def get_one_by_id(self, id: int):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        try:
            return result.scalar_one()
        except NoResultFound:
            raise HTTPException(status_code=400, detail=f"Запись не найдена")

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]


    async def delete_one(self, data_id):
        stmt = delete(self.model).where(self.model.id == data_id).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()
