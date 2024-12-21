from fastapi import APIRouter,Depends
from typing import Annotated

from src.api.dependencies import borrows_service
from src.schemas.borrows import BorrowSchemaAdd, BorrowSchema, BorrowsSchemaReturn
from src.services.borrows import BorrowsService

router = APIRouter(
    prefix="/borrows",
    tags=["Выдача"],
)


@router.get("", summary="Получить все выданные книги")
async def get_all_borrows(get_borrows_service: Annotated[BorrowsService, Depends(borrows_service)]) -> list[BorrowSchema]:
    result = await get_borrows_service.find_all_borrows()
    return result

@router.post("", summary="Выдать книгу")
async def create_borrows(borrow: BorrowSchemaAdd, get_borrows_service: Annotated[BorrowsService, Depends(borrows_service)]) -> BorrowSchemaAdd:
    borrow_result = await get_borrows_service.add_borrow(borrow)
    return borrow_result

@router.delete("/{id}", summary="Удалить выдачу")
async def delete_borrows(id: int, get_borrows_service: Annotated[BorrowsService, Depends(borrows_service)]) -> BorrowSchema:
    result = await get_borrows_service.delete_borrows_by_id(id)
    return result

@router.patch("/{id}/return", summary="Вернуть книгу")
async def return_borrows(id: int, return_data: BorrowsSchemaReturn, get_borrows_service: Annotated[BorrowsService, Depends(borrows_service)]) -> BorrowSchema:
    result = await get_borrows_service.return_borrows_by_id(id, return_data)
    return result

