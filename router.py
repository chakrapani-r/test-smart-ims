from fastapi import APIRouter, HTTPException, Path, Depends
from dbconfig import SessionLocal
from sqlalchemy.orm import Session

from schemas import BookSchema, RequestBook, Response
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/create')
async def create(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, request.parameter)
    return Response(code=200, status="ok", message="Book created successfully").dict(exclude_none=True)


@router.get('/')
async def get(db: Session = Depends(get_db)):
    _books = crud.get_books(db, 0, 100)
    return Response(code=200, status="ok", message="Successfully fetched all books", result=_books).dict(exclude_none=True)


@router.get('/{id}}')
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _book = crud.get_book_by_id(db=db, book_id=id)
    return Response(code=200, status="ok", message="Successfully fetched the book", result=_book).dict(exclude_none=True)


@router.post('/update')
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(db=db, book_id=request.parameter.id, title=request.parameter.title, description=request.parameter.description)
    return Response(code=200, status="ok", message="Successfully updated the book", result=_book)


@router.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)):
    crud.remove_book(db=db, book_id=id)
    return Response(code=200, status="ok", message="Successfully deleted the book").dict(exclude_none=True)
