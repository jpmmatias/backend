from contextlib import asynccontextmanager
from fastapi import FastAPI
from utils.init_db import create_tables
from router import api

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    debug=True,
    title="Todo List",
    lifespan=lifespan
)


    

app.include_router(api.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo List API"}