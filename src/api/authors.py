from http.client import HTTPException

from fastapi import APIRouter, Depends
from typing import Annotated


from src.schemas.authors import AuthorsSchemaAdd, AuthorsSchemaDelete

from src.api.dependencies import item_service
from src.services.authors import AuthorService

router = APIRouter(
    tags=["Авторы"],
    prefix="/authors",
)


@router.post("", summary="Добавление нового автора")
async def create_authors(item: AuthorsSchemaAdd, get_item_service: Annotated[AuthorService, Depends(item_service)]):
    item_result = await get_item_service.add_item(item)
    return {"item_result": item_result}

@router.get("", summary="Получить всеъ авторов")
async def get_all_authors(get_item_service: Annotated[AuthorService, Depends(item_service)]):
    result = await get_item_service.find_all_items()
    return {"all_items": result}

@router.get("/{id}", summary="Получить всех авторов по id")
async def get_authors_by_id(item_id: int ,get_item_service: Annotated[AuthorService, Depends(item_service)]):
    result = await get_item_service.get_item_by_id(item_id)
    return {"all_items": result}

@router.delete("", summary="Удаление автора")
async def delete_authors(item_id: AuthorsSchemaDelete, get_item_service: Annotated[AuthorService, Depends(item_service)]):
    result = await get_item_service.delete_item(item_id)
    return {"delete_item": result}

