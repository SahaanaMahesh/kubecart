from fastapi import FastAPI

from .database import engine, Base
from .models import Product
from .routes.products import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service")

app.include_router(router)

@app.get("/")
def root():
    return {"service": "product-service"}