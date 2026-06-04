from fastapi import FastAPI

from .database import engine, Base
from .models import User

from .routes.users import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KubeCart User Service"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "service": "user-service"
    }