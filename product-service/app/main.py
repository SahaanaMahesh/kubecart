from fastapi import FastAPI

from .database import engine, Base
from .routes.products import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service")

app.include_router(router)