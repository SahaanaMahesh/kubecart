from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app = FastAPI(
    title="KubeCart API Gateway"
)

USER_SERVICE = "http://localhost:8000"
PRODUCT_SERVICE = "http://localhost:8001"
ORDER_SERVICE = "http://localhost:8003"
REVIEW_SERVICE = "http://localhost:8004"
CHATBOT_SERVICE = "http://localhost:8005"


@app.get("/")
def root():
    return {
        "service": "api-gateway"
    }


# -----------------
# PRODUCTS
# -----------------

@app.get("/products")
async def get_products():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{PRODUCT_SERVICE}/products"
        )

    return response.json()


# -----------------
# ORDERS
# -----------------

@app.get("/orders")
async def get_orders():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{ORDER_SERVICE}/orders"
        )

    return response.json()


# -----------------
# REVIEWS
# -----------------

@app.get("/reviews")
async def get_reviews():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{REVIEW_SERVICE}/reviews"
        )

    return response.json()


# -----------------
# CHATBOT
# -----------------

@app.post("/chat")
async def chat(payload: dict):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{CHATBOT_SERVICE}/chat",
            json=payload
        )

    return response.json()