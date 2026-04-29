import os
import time
from datetime import datetime, timezone
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from pydantic import BaseModel

from agents import get_agent, get_all_agents

load_dotenv()

app = FastAPI(title="BearBot AI Backend", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# In-memory session storage: { sessionId: { history: [...], last_active: float } }
chat_sessions: dict = {}


class MessageRequest(BaseModel):
    message: str
    sessionId: str
    studentYear: Optional[str] = "Freshman"


class ClearRequest(BaseModel):
    sessionId: str


def _get_or_create_session(session_id: str) -> dict:
    if session_id not in chat_sessions:
        chat_sessions[session_id] = {"history": [], "last_active": time.time()}
    return chat_sessions[session_id]


def _cleanup_old_sessions() -> None:
    now = time.time()
    expired = [k for k, v in chat_sessions.items() if now - v["last_active"] > 3600]
    for k in expired:
        del chat_sessions[k]


@app.post("/api/chat/message")
async def send_message(request: MessageRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    if len(request.message) > 2000:
        raise HTTPException(
            status_code=400,
            detail="Message too long. Please keep it under 2000 characters."
        )

    session = _get_or_create_session(request.sessionId)
    session["last_active"] = time.time()
    history = session["history"]

    # Prefix first message with student year context
    enriched_message = request.message
    if request.studentYear and len(history) == 0:
        enriched_message = f"[Student Year: {request.studentYear}] {request.message}"

    agent = get_agent(request.studentYear)

    messages = [
        {"role": "system", "content": agent["system_prompt"]},
        *history,
        {"role": "user", "content": enriched_message},
    ]

    # Keep last 20 message pairs to avoid token overflow (system + 40 history)
    if len(messages) > 41:
        messages = [messages[0]] + messages[-40:]

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
            temperature=0.85,
        )

        text = response.choices[0].message.content

        history.append({"role": "user", "content": enriched_message})
        history.append({"role": "assistant", "content": text})

        if len(history) > 40:
            session["history"] = history[-40:]

        _cleanup_old_sessions()

        return {
            "message": text,
            "sessionId": request.sessionId,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": {
                "name": agent["name"],
                "emoji": agent["emoji"],
                "tagline": agent["tagline"],
            },
        }

    except Exception as e:
        print(f"Groq API Error: {e}")
        raise HTTPException(
            status_code=500,
            detail="BearBot is temporarily unavailable. Please try again or contact advising at scmns.advising@morgan.edu",
        )


@app.post("/api/chat/clear")
async def clear_chat(request: ClearRequest):
    if request.sessionId in chat_sessions:
        del chat_sessions[request.sessionId]
    return {"success": True, "message": "Conversation cleared"}


@app.get("/api/chat/health")
async def health():
    return {
        "status": "ok",
        "bot": "BearBot",
        "university": "Morgan State University",
        "backend": "Python FastAPI + Groq AI",
    }


@app.get("/api/agents")
async def list_agents():
    """Return metadata for all available agents."""
    return {"agents": get_all_agents()}


@app.get("/")
async def root():
    return {"message": "BearBot Python AI Backend is running. Go Bears!"}
