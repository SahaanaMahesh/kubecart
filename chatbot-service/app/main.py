from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Headphones", "price": 2000},
    {"id": 3, "name": "Mouse", "price": 500},
]

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.lower()

    if "laptop" in message:
        return {
            "response": "I recommend the Laptop.",
            "products": [products[0]]
        }

    if "audio" in message or "headphone" in message:
        return {
            "response": "You may like these headphones.",
            "products": [products[1]]
        }

    return {
        "response": "Here are some products you may like.",
        "products": products
    }