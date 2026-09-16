from fastapi import FastAPI
from pydantic import BaseModel

from chat import generate_response
from coder import generate_code, explain_code, fix_code
from images import create_image_prompt


app = FastAPI(
    title="Nexa AI",
    description="Nexa AI – chatbot, AI programátor a generovanie obrázkov",
    version="0.2.0",
)


# -------------------------
# Request models
# -------------------------

class ChatRequest(BaseModel):
    message: str


class CodeRequest(BaseModel):
    request: str


class CodeBody(BaseModel):
    code: str


class ImageRequest(BaseModel):
    description: str


# -------------------------
# Basic endpoints
# -------------------------

@app.get("/")
def home():
    return {
        "name": "Nexa AI",
        "status": "online",
        "version": "0.2.0",
        "features": [
            "chat",
            "programming",
            "image generation",
        ],
    }


@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# Chat
# -------------------------

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "response": generate_response(request.message)
    }


# -------------------------
# AI Programmer
# -------------------------

@app.post("/code/generate")
def code_generate(request: CodeRequest):
    return {
        "response": generate_code(request.request)
    }


@app.post("/code/explain")
def code_explain(request: CodeBody):
    return {
        "response": explain_code(request.code)
    }


@app.post("/code/fix")
def code_fix(request: CodeBody):
    return {
        "response": fix_code(request.code)
    }


# -------------------------
# Image generation
# -------------------------

@app.post("/images")
def generate_image(request: ImageRequest):
    return {
        "prompt": create_image_prompt(request.description)
    }
