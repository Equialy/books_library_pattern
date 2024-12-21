from pydantic import BaseModel, Field
from datetime import date

from sqlalchemy import Date


class AuthorsSchema(BaseModel):
    id: int = Field(..., ge=1 )
    name: str = Field(..., min_length=1, max_length=100 )
    second_name: str = Field(..., min_length=1, max_length=100)
    birthday: date = Field(..., le=date.today())

    class Config:
        from_attributes = True

class AuthorsSchemaAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100 )
    second_name: str = Field(..., min_length=1, max_length=100)
    birthday: date = Field(..., le=date.today())

    class Config:
        from_attributes = True

class AuthorsSchemaDelete(BaseModel):
    id: int
