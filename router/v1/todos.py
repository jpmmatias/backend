from typing import List

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.Todo import TodoSchema 
from services.todo_service import TodoService 


router = APIRouter(
    prefix="/todos",
    tags=["todo"]

)


@router.post("", status_code=201, response_model=TodoSchema)
def create_todo(
        data: TodoSchema,
        session: Session = Depends(get_db),
):
    _service = TodoService(session)
    return _service.create(data)


@router.get("", status_code=200, response_model=List[TodoSchema])
def get_todos(session: Session = Depends(get_db)) -> List[TodoSchema]:
    _service = TodoService(session)
    return _service.get_all()


@router.delete("/{_id}", status_code=204)
def delete_todo(
        _id: UUID4,
        session: Session = Depends(get_db),
):
    _service = TodoService(session)
    return _service.delete(_id)


@router.put("/{_id}", status_code=200, response_model=TodoSchema)
def update_todo(
        _id: UUID4,
        data: TodoSchema,
        session: Session = Depends(get_db),
):
    _service = TodoService(session)
    return _service.update(_id, data)