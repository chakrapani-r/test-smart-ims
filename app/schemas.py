from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
#from pydantic.BaseModel import GenericModel
#from pydantic.generics import GenericModel

T = TypeVar('T')


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True
#        orm_mode = True


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None
