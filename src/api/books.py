from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.api.dependencies import books_service
from src.models.books import Books
from src.schemas.books import BooksSchemaAdd, BookSchema, BookResponse, BookSchemaDelete
from src.services.books import BookService

router = APIRouter(
    prefix="/books",
    tags=["Книги"],
)


@router.post("", summary="Добавление новой книги")
async def create_books(book: BooksSchemaAdd, get_books_service: Annotated[BookService, Depends(books_service)]):
    book_result = await get_books_service.add_one_book(book)
    return {"book_result": book_result}


@router.get("", summary="Получить все книги")
async def get_all_books(get_books_service: Annotated[BookService, Depends(books_service)]):
    book_result = await get_books_service.find_all_books()
    return {"all_books": book_result}


@router.get("/{id}", summary="Получить книгу по id")
async def get_books_by_id(id_book: int, get_books_service: Annotated[BookService, Depends(books_service)]) -> BookResponse:
    result = await get_books_service.get_book_by_id(id_book)
    return {"book": result}

@router.delete("/{id}", summary="Удаление книги")
async def delete_book(id: int, get_books_service: Annotated[BookService, Depends(books_service)]):
    result = await get_books_service.delete_books_by_id(id)
    return {"delete_book": result}

