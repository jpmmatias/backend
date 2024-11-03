from typing import List, Optional

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from repositories.todo_repository import  TodoRepository
from schemas.Todo import TodoSchema 


class TodoService:
    def __init__(self, session: Session):
        self.repository = TodoRepository(session)

    def create(self, data: TodoSchema) -> TodoSchema:
        return self.repository.create(data)

    def get_all(self) -> List[Optional[TodoSchema]]:
        return self.repository.get_all()

    def delete(self, _id: UUID4) -> bool:
        if not self.repository.todo_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="Todo not found")
        todo = self.repository.get_by_id(_id)
        self.repository.delete(todo)
        return True

    def update(self, _id: UUID4, data: TodoSchema) -> TodoSchema:
        if not self.repository.todo_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="Todo not found")
        todo = self.repository.get_by_id(_id)
        return self.repository.update(todo, data)