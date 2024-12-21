from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from src.db.db import get_async_session

from src.repositories.authors import AuthorRepository
from src.repositories.books import BooksRepository
from src.repositories.borrows import BorrowsRepository
from src.services.authors import AuthorService
from src.services.books import BookService
from src.services.borrows import BorrowsService


def item_service(session : AsyncSession = Depends(get_async_session)):
    return AuthorService(AuthorRepository(session))

def books_service(session: AsyncSession = Depends(get_async_session)):
    return BookService(BooksRepository(session))

def borrows_service(session: AsyncSession = Depends(get_async_session)):
    return BorrowsService(BorrowsRepository(session))