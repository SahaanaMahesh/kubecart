from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="KubeCart Chatbot Service"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "service": "chatbot-service"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    msg = request.message.lower()

    if "laptop" in msg:
        return {
            "response": "I recommend MacBook Air."
        }

    elif "phone" in msg:
        return {
            "response": "I recommend iPhone 15."
        }

    elif "electronics" in msg:
        return {
            "response": "Check our Electronics category."
        }

    return {
        "response": f"You said: {request.message}"
    }