from fastapi import FastAPI

from contextlib import asynccontextmanager

from .routes import products
from .database.db_config import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(products.apiRouter)