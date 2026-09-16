from fastapi import FastAPI
from pydantic import BaseModel

from chat import generate_response


app = FastAPI(
    title="Nexa AI",
    description="Nexa AI – chatbot, AI programátor a generovanie obrázkov",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def home():
    return {
        "name": "Nexa AI",
        "status": "online",
        "version": "0.1.0",
        "features": [
            "chat",
            "programming",
            "image generation",
        ],
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = generate_response(request.message)

    return ChatResponse(
        response=response
    )
