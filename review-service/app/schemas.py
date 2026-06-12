from pydantic import BaseModel


class ReviewCreate(BaseModel):
    user_id: int
    product_id: int
    rating: int
    comment: str