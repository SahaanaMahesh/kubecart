from fastapi import FastAPI

from .database import Base, engine
from .routes.reviews import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Review Service")
app.include_router(router)


@app.get("/")
def root():
    return {"service": "review-service"}