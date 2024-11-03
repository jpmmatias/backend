from fastapi import APIRouter
from router.v1 import todos

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(todos.router)