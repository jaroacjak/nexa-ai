from fastapi import FastAPI
from pydantic import BaseModel

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
    message = request.message.strip()

    if not message:
        return ChatResponse(
            response="Ahoj! Som Nexa AI. Napíš mi správu."
        )

    # TODO: Neskôr sem pripojíme skutočný AI model.
    return ChatResponse(
        response=f"Nexa AI rozumie tvojej správe: {message}"
    )
