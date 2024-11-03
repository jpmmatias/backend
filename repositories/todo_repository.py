from sqlalchemy.orm import Session
from models.Todo import Todo
from schemas.Todo import TodoSchema
from typing import List, Optional, Type
from pydantic import UUID4


class TodoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: TodoSchema) -> TodoSchema:
        todo = Todo(**data.model_dump(exclude_none=True))
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return TodoSchema(id=todo.id, content=todo.content, complete=todo.complete)

    def get_all(self) -> List[Optional[TodoSchema]]:
        todos = self.session.query(Todo).all()
        return [TodoSchema(**todo.__dict__) for todo in todos]  

    def get_todo(self, _id: UUID4) -> TodoSchema:
        todo = self.session.query(Todo).filter_by(id=_id).first()
        return TodoSchema(**todo.__dict__)

    def get_by_id(self, _id: UUID4) -> Type[TodoSchema]:
        return self.session.query(Todo).filter_by(id=_id).first()

    def todo_exists_by_id(self, _id: UUID4) -> bool:
        todo = self.session.query(Todo).filter_by(id=_id).first()
        return todo is not None

    def update(self, todo: Type[Todo], data: TodoSchema) -> TodoSchema:
        todo.content = data.content
        todo.complete = data.complete
        self.session.commit()
        self.session.refresh(todo)
        return TodoSchema(**todo.__dict__)

    def delete(self, todo: Type[Todo]) -> bool:
        self.session.delete(todo)
        self.session.commit()
        return True
