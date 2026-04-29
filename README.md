# BearBot — Morgan State CS Academic Advisor

An AI-powered chatbot for Morgan State University Computer Science students.  
Helps with advising, course planning, campus resources, internships, study strategies, and more.

**Stack:** React + Vite (frontend) · Node.js + Express (server/proxy) · Python FastAPI (AI backend) · Groq AI (LLM)

---

## AGENTS

BearBot uses three AI personas, each tailored to a student's academic year:

| Agent | Years | Personality | Focus Areas |
|---|---|---|---|
| 🌱 **Coach Bear** | Freshman (0–29 credits) | Warm, patient, encouraging | COSC 111/112, gen ed, orientation, FAFSA, Banner |
| 💻 **Dev Bear** | Sophomore/Junior (30–89 credits) | Energetic, direct, motivating | Data Structures, internships, career prep, electives |
| 🎓 **Cap Bear** | Senior (90+ credits) | Calm, focused, strategic | COSC 490, graduation requirements, job offers, grad school |

Each agent is grounded by a **Sourcing Rules** system:
- **TYPE A questions** (Morgan-specific facts: courses, deadlines, policies) — answered only from the knowledge base, never fabricated
- **TYPE B questions** (general CS: algorithms, study tips, career advice) — answered fully using AI knowledge

---

## PROJECT STRUCTURE

```
morgan-cs-advisor/
├── client/                        ← React + Vite frontend
│   ├── src/
│   │   ├── App.jsx                ← Main app component (state, sessions, API calls)
│   │   ├── main.jsx               ← React entry point
│   │   ├── styles/main.css        ← MSU Blue & Gold theme
│   │   └── components/
│   │       ├── Sidebar.jsx        ← Year selector, quick questions, agent card, contact info
│   │       ├── ChatWindow.jsx     ← Message list + welcome screen
│   │       ├── MessageBubble.jsx  ← Individual chat messages (markdown rendered)
│   │       ├── InputBar.jsx       ← Text input + send button (2000 char limit)
│   │       └── TypingIndicator.jsx ← Animated "BearBot is typing" indicator
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
├── server/                        ← Node.js Express server
│   ├── server.js                  ← Serves React build + proxies /api to Python backend
│   ├── .env                       ← PYTHON_API_URL, PORT
│   └── package.json
│
├── backend/                       ← Python FastAPI AI backend
│   ├── main.py                    ← FastAPI app + chat endpoints + session management
│   ├── agents.py                  ← Three AI agents (Coach Bear, Dev Bear, Cap Bear)
│   ├── knowledge.py               ← Morgan State curriculum & campus knowledge base
│   ├── requirements.txt           ← Python dependencies
│   └── .env                       ← GROQ_API_KEY (never commit this)
│
├── package.json                   ← Root scripts (npm run dev, install:all, etc.)
├── render.yaml                    ← Render.com deployment config
└── .gitignore
```

---

## HOW IT WORKS

```
User opens browser
      ↓
React App (Vite, port 5173)
      ↓  POST /api/chat/message  { message, sessionId, studentYear }
Node.js Express (port 3001)    ← proxies /api/* to Python
      ↓  http://localhost:8000
Python FastAPI (port 8000)
      ↓  routes to correct agent (Coach/Dev/Cap Bear)
      ↓  assembles system prompt + conversation history
Groq AI (llama-3.3-70b-versatile)
      ↓  returns AI response
Python → Node → React
      ↓
MessageBubble renders response as markdown
```

**Session Management:**
- Browser generates a UUID stored in `sessionStorage` (survives refresh, clears on tab close)
- Python keeps conversation history in memory (last 20 message pairs per session)
- Sessions expire after 1 hour of inactivity

---

## QUICK START — Run Locally

### Step 1: Get a Groq API Key (Free)

1. Go to https://console.groq.com
2. Sign up → Dashboard → API Keys → Create API Key
3. Copy the key

### Step 2: Add Your API Key

Open `backend/.env` and add:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Step 3: Install All Dependencies

Open a terminal in VS Code (`Ctrl + \``) and run:

```bash
npm run install:all
```

This installs Node.js deps for root + server + client, and Python deps for backend.

> **Requires:** Node.js 18+, Python 3.9+, pip

### Step 4: Start Everything

```bash
npm run dev
```

This starts all three services at once:
- Python AI backend → http://localhost:8000
- Node.js server    → http://localhost:3001
- React dev server  → http://localhost:5173

### Step 5: Open in Browser

Go to: **http://localhost:5173**

---

## DEPLOYMENT — Render.com (Free, No Credit Card)

This project uses two free Render services (configured in `render.yaml`).

> Free Render services sleep after 15 min of inactivity. First load may take ~30 seconds to wake up.

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Deploy BearBot"
git push origin main
```

### Step 2: Deploy Python AI Backend

1. Go to https://render.com → New → Web Service
2. Connect your GitHub repo
3. **Name:** `bearbot-api`
4. **Runtime:** Python
5. **Root Directory:** `backend`
6. **Build Command:** `pip install -r requirements.txt`
7. **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
8. Add environment variable: `GROQ_API_KEY` = your key
9. Deploy → copy the URL (e.g. `https://bearbot-api.onrender.com`)

### Step 3: Deploy Node.js Web Server

1. New → Web Service
2. Connect the same GitHub repo
3. **Name:** `bearbot-web`
4. **Runtime:** Node
5. **Build Command:** `npm install && cd server && npm install && cd ../client && npm install && npm run build`
6. **Start Command:** `npm start`
7. Add environment variable: `PYTHON_API_URL` = the URL from Step 2
8. Deploy → your app is live!

---

## CUSTOMIZING BEARBOT

### Update the Knowledge Base

Edit `backend/knowledge.py` to add:
- New courses or professors
- Updated deadlines and policies
- Additional campus resources
- Club and event information

### Change an Agent's Personality

Edit the system prompts in `backend/agents.py`:
- `CoachBearAgent` — Freshman advisor
- `DevBearAgent` — Sophomore/Junior advisor
- `CapBearAgent` — Senior advisor

### Update the Theme

Edit `client/src/styles/main.css`:
- `--msu-blue: #003087` — Morgan State Blue
- `--msu-gold: #F5A623` — Morgan State Gold

### Add Quick Action Buttons

Edit the `quickActions` object in `client/src/components/Sidebar.jsx` — each key maps to a student year.

---

## TROUBLESHOOTING

**"Module not found" error:**  
Run `npm run install:all` again.

**Python backend not starting:**  
Make sure Python 3.9+ and pip are installed. Try:  
`cd backend && pip install -r requirements.txt && uvicorn main:app --port 8000`

**"Invalid API key" error:**  
Double-check `backend/.env` — no extra spaces or quotes around the key.

**Port already in use:**  
Change `PORT=3001` in `server/.env` or `PORT=8000` in `backend/.env`.

**Blank screen in browser:**  
Make sure all three servers are running. Check browser console (F12) for errors.

**Bot gives wrong Morgan-specific info:**  
Update the relevant section in `backend/knowledge.py` and restart the backend.

---

## CONTACT & RESOURCES

**Academic Advising:**  
Center for Academic Success and Achievement (CASA)  
Tyler Hall, Suite 117 · 1700 E. Cold Spring Lane · Baltimore, MD 21251  
Phone: 443-885-3380 · Email: CASA@morgan.edu

**Tech Resources:**
- Groq API (free LLM): https://console.groq.com
- Render free hosting: https://render.com
- FastAPI docs: https://fastapi.tiangolo.com
- Vite + React docs: https://vitejs.dev

**Go Bears! 🐻**
