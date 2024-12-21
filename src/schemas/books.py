from pydantic import BaseModel,Field


class BookSchema(BaseModel):
    id: int = Field(..., ge=1 )
    title: str = Field(..., min_length=1, max_length=50)
    describe: str = Field(..., min_length=1, max_length=256)
    id_author: int = Field(..., ge=1)
    quantity: int = Field(..., ge=0)

    class Config:
        from_attributes = True

class BooksSchemaAdd(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    describe: str = Field(..., min_length=1, max_length=50)
    id_author: int = Field(..., ge=1)
    quantity: int = Field(..., ge=0)


class BookSchemaDelete(BaseModel):
    id: int = Field(..., ge=1)

class BookResponse(BaseModel):
    book: BookSchema