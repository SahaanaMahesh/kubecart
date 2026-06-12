from fastapi import FastAPI

from .database import Base
from .database import engine

from .routes.orders import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KubeCart Order Service"
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "service": "order-service"
    }