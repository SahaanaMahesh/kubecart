from fastapi import FastAPI
from threading import Thread

from .database import Base
from .database import engine

from .routes.recommendations import router

from .kafka_consumer import consume

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KubeCart Recommendation Service"
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "service": "recommendation-service"
    }


@app.on_event("startup")
def startup():

    Thread(
        target=consume,
        daemon=True
    ).start()