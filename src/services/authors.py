from src.models.authors import Authors
from src.repositories.authors import AuthorRepository
from src.schemas.authors import AuthorsSchema, AuthorsSchemaAdd, AuthorsSchemaDelete
from src.utils.repository import AbstractRepository


class AuthorService:
    def __init__(self, item_repo: AuthorRepository):
        self.item_repo: AuthorRepository = item_repo

    async def add_item(self, item: AuthorsSchemaAdd) -> Authors:
        item_dict = item.model_dump()
        item_result = await self.item_repo.add_one(item_dict)
        return item_result

    async def get_item_by_id(self, id: int) -> Authors:
        item_result = await self.item_repo.get_one_by_id(id)
        return item_result


    async def find_all_items(self):
        item_result = await self.item_repo.find_all()
        return item_result

    async def delete_item(self, item_id: AuthorsSchemaDelete) -> AuthorsSchema:
        item_dict = item_id.model_dump()
        item_result = await self.item_repo.delete_one(item_dict)
        return item_result


