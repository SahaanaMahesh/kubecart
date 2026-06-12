from pydantic import BaseModel


class RecommendationResponse(BaseModel):

    product_id: int
    product_name: str
    category: str