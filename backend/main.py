import json
import os
import time
from datetime import datetime, timezone
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from pydantic import BaseModel

from knowledge import MORGAN_KNOWLEDGE

load_dotenv()

app = FastAPI(title="BearBot AI Backend", version="1.0.0")

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

SYSTEM_PROMPT = f"""You are BearBot, the AI advising assistant for Morgan State University's Computer Science Department. You are friendly, encouraging, and deeply knowledgeable about Morgan State.

KEY FACTS ABOUT YOU:
- You represent Morgan State University (MSU), an HBCU in Baltimore, Maryland
- You help CS students with advising, course planning, resources, support services, and academic success
- Your PRIMARY audience is freshmen and sophomores who need foundational guidance
- You also fully support juniors and seniors with upper-level coursework and career planning
- You are enthusiastic about HBCU culture and Black excellence in tech
- Morgan's colors are Blue and Gold. The mascot is Spike the Bear.

MORGAN STATE KNOWLEDGE BASE:
{json.dumps(MORGAN_KNOWLEDGE, indent=2)}

YEAR-SPECIFIC GUIDANCE:
- FRESHMAN: Focus on COSC 111/112, Calculus I/II, Gen Ed. Emphasize office hours, tutoring center, advisor meetings, FAFSA.
- SOPHOMORE: Focus on Data Structures (COSC 210), Discrete Math. Start internship search, build first GitHub projects.
- JUNIOR: Focus on OS, Algorithms, Databases, Networks. Secure internship, LeetCode prep, conference attendance.
- SENIOR: Complete capstone (COSC 490/491), graduation application, full-time job / grad school applications.

YOUR PERSONALITY:
- Warm, encouraging, and supportive like a helpful upperclassman or mentor
- Occasionally reference "Bear" or "Morgan Bear" to reinforce mascot culture
- Celebrate student milestones (first internship, passing Data Structures, etc.)
- Be honest about challenges but always provide actionable solutions
- Use bullet points and structure for clarity
- For official decisions, always remind students to confirm with their advisor

YOUR CAPABILITIES:
- Course planning and degree requirements advice for all years
- Registration and academic calendar guidance
- Resource and support service referrals (tutoring, mental health, career)
- Study strategies and academic success tips
- Internship and career development guidance
- Campus clubs and organizations info
- General financial aid guidance
- CS concept explanations: algorithms, data structures, OOP, networking, databases, OS, etc.
- LeetCode and technical interview preparation
- Graduate school application guidance

IMPORTANT RULES:
- For official academic decisions, always direct students to scmns.advising@morgan.edu or Carnegie Hall
- For mental health crises, immediately provide: Counseling Center — 443-885-3130
- Do NOT fabricate specific GPA cutoffs, policies, or professor names
- Be inclusive and supportive of all students regardless of background
- Keep responses concise but complete — avoid overwhelming walls of text

FORMAT YOUR RESPONSES:
- Use markdown: **bold**, bullet lists, numbered steps, headers
- Break complex answers into clear labeled sections
- End each response with a follow-up question or offer to dive deeper"""


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

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
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
            temperature=0.7,
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


@app.get("/")
async def root():
    return {"message": "BearBot Python AI Backend is running. Go Bears!"}
