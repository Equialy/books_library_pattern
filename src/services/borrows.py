from fastapi import HTTPException

from src.models.borrows import Borrows
from src.repositories.borrows import BorrowsRepository
from src.schemas.borrows import BorrowSchemaAdd, BorrowsSchemaDelete, BorrowSchema, BorrowsSchemaUpdate, \
    BorrowsSchemaReturn


class BorrowsService:
    def __init__(self, borrow_repo: BorrowsRepository):
        self.borrow_repo: BorrowsRepository = borrow_repo

    def _validate_borrow_id(self, borrow_id: int):
        if borrow_id <= 0:
            raise HTTPException(status_code=404, detail="Параметр id должен быть больше 0.")


    async def add_borrow(self, borrow_data: BorrowSchemaAdd) -> Borrows:
        borrow_result = await self.borrow_repo.add_one(borrow_data)
        return borrow_result

    async def find_all_borrows(self) -> list[Borrows]:
        result = await self.borrow_repo.find_all()
        return result

    async def return_borrows_by_id(self, borrow_id: int, date_return) -> Borrows:
        self._validate_borrow_id(borrow_id)
        borrow_book = await self.borrow_repo.get_one_by_id(borrow_id)
        if borrow_book.date_return is not None:
            raise HTTPException(status_code=400, detail="Книга уже возвращена.")
        if date_return.date_return < borrow_book.date_borrow:
            raise HTTPException(status_code=400, detail="Дата возврата не может быть раньше даты выдачи.")

        result = await self.borrow_repo.return_borrows(borrow_id, date_return)
        return result

    # async def delete_borrows_by_id(self, id_borrow: int) -> Borrows:
    #     self._validate_borrow_id(id_borrow)
    #     result = await self.borrow_repo.delete_one(id_borrow)
    #     return result
