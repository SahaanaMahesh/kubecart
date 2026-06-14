from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="KubeCart API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCT_SERVICE = "http://localhost:8001"
ORDER_SERVICE = "http://localhost:8003"
REVIEW_SERVICE = "http://localhost:8004"
CHATBOT_SERVICE = "http://localhost:8005"


@app.get("/")
def root():
    return {"service": "api-gateway"}


# -------------------------
# Product Service
# -------------------------

@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE}/products")
        response.raise_for_status()
    return response.json()


@app.post("/products")
async def create_product(product: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{PRODUCT_SERVICE}/products", json=product)
        response.raise_for_status()
    return response.json()


# -------------------------
# Order Service
# -------------------------

@app.get("/orders")
async def get_orders():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ORDER_SERVICE}/orders")
        response.raise_for_status()
    return response.json()


@app.post("/orders")
async def create_order(order: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ORDER_SERVICE}/orders", json=order)
        response.raise_for_status()
    return response.json()


# -------------------------
# Review Service
# -------------------------

@app.post("/reviews")
async def create_review(review: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{REVIEW_SERVICE}/reviews", json=review)
        response.raise_for_status()
    return response.json()


@app.get("/reviews")
async def get_all_reviews():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{REVIEW_SERVICE}/reviews")
        response.raise_for_status()
    return response.json()


@app.get("/reviews/{product_id}")
async def get_reviews(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{REVIEW_SERVICE}/reviews/{product_id}")
        response.raise_for_status()
    return response.json()


# -------------------------
# Chatbot Service
# -------------------------

@app.post("/chat")
async def chat(request: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{CHATBOT_SERVICE}/chat", json=request)
        response.raise_for_status()
    return response.json()