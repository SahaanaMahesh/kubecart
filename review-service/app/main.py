from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

reviews = []

class Review(BaseModel):
    product_id: int
    username: str
    rating: int
    comment: str

@app.post("/reviews")
def add_review(review: Review):
    reviews.append(review.dict())
    return {"message": "Review added successfully"}

@app.get("/reviews/{product_id}")
def get_reviews(product_id: int):
    return [
        review
        for review in reviews
        if review["product_id"] == product_id
    ]