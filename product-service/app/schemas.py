from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    seller_id: str


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    seller_id: str

    class Config:
        from_attributes = True