
from pydantic import BaseModel
from uuid import UUID

class TodoSchema(BaseModel):
    id: UUID
    content: str
    complete: bool = False
    
