from src.models.books import Books
from src.repositories.books import BooksRepository
from src.schemas.books import BooksSchemaAdd, BookSchema, BookSchemaDelete


class BookService:
    def __init__(self, book_repo: BooksRepository):
        self.book_repo: BooksRepository = book_repo

    async def find_all_books(self):
        book_result = await self.book_repo.find_all()
        return book_result

    async def add_one_book(self, book: BooksSchemaAdd):
        book_dict = book.model_dump()
        book_result = await self.book_repo.add_one(book_dict)
        return book_result

    async def get_book_by_id(self, id: int) -> Books:
        book_result = await self.book_repo.get_one_by_id(id)
        return book_result

    async def delete_books_by_id(self, book_id: int) -> BookSchema:

        book_result = await self.book_repo.delete_one(book_id)
        return book_result