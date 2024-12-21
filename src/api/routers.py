from src.api.authors import router as router_authors
from src.api.books import router as router_books
from src.api.borrows import router as router_borrows


all_router = [
    router_authors,
    router_books,
    router_borrows
]