#  Digital FTE — AI Content Agent

A mini autonomous AI agent that plans, writes, and **critiques its own work** — generating platform-specific social media content from a single topic input. Built with **LangChain**, **Google Gemini API**, and **FastAPI**.

This was built as a technical assessment task demonstrating a self-correcting multi-agent pipeline: a "Digital FTE" (Full-Time Equivalent) that can take a user input and autonomously perform a complete content-creation task end to end.

---

##  What It Does

Give it a topic — e.g. *"benefits of AI agents for startups"* — and it will:

1. **Plan** a content strategy (audience, tone, key message, call-to-action)
2. **Write** a platform-specific post for each platform you choose (LinkedIn, Twitter, etc.)
3. **Critique** its own draft, score it, and automatically produce an improved final version
4. Return strategy, draft, final post, and critic feedback — all in one structured response

No human editing required between steps — the agent self-corrects before returning output.

---

##  Architecture

```
User Input (topic + platforms)
            │
            ▼
   ┌─────────────────┐
   │  Planner Agent    │  → creates one shared content strategy
   └────────┬──────────┘
            │
   for each selected platform:
            ▼
   ┌─────────────────┐
   │  Writer Agent     │  → drafts a platform-specific post
   └────────┬──────────┘
            ▼
   ┌─────────────────┐
   │  Critic Agent     │  → reviews the draft, gives feedback,
   │                   │     and produces an improved final post
   └────────┬──────────┘
            ▼
   Final structured response (strategy + per-platform results)
```

One shared strategy feeds multiple platform-specific writer/critic passes — so the same campaign idea is adapted to each platform's tone and length, not just copy-pasted.

---

##  Project Structure

```
digital-fte-agent/
├── agents/
│   ├── planner.py        # Generates the content strategy
│   ├── writer.py          # Drafts platform-specific posts
│   ├── critic.py            # Reviews & refines the draft
│   └── utils.py               # Safely extracts text from LLM responses
│
├── services/
│   └── workflow.py              # Orchestrates planner → writer → critic per platform
│
├── models/
│   └── schemas.py                 # Pydantic request/response schemas
│
├── api/
│   └── routes.py                    # POST /api/generate endpoint
│
├── static/
│   └── index.html                     # Simple browser UI to test the agent
│
├── main.py                              # FastAPI app entrypoint
├── requirements.txt
└── .env.example
```

---

##  Getting Started

### 1. Clone & install

```bash
git clone https://github.com/bilalrafique5/digital-fte-agent.git
cd digital-fte-agent

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

### 2. Set up your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

### 3. Run the backend

```bash
uvicorn main:app --reload
```

API runs at **http://127.0.0.1:7000** — interactive docs at **http://127.0.0.1:7000/docs**.

### 4. Run the UI (optional)

Open `static/index.html` directly in your browser, or serve it with Live Server / `python -m http.server` — it calls the local API and renders results visually.

---

##  API

### `POST /api/generate`

**Request:**
```json
{
  "topic": "benefits of AI agents for startups",
  "platforms": ["LinkedIn", "Twitter"]
}
```

**Response:**
```json
{
  "status": "success",
  "strategy": "Audience & tone, key message, and CTA for this topic",
  "results": {
    "LinkedIn": {
      "draft": "...",
      "final_post": "...",
      "critic_feedback": "..."
    },
    "Twitter": {
      "draft": "...",
      "final_post": "...",
      "critic_feedback": "..."
    }
  }
}
```

Works with any number of platforms — pass just `["LinkedIn"]` for a single-platform post, or add more (e.g. `"Instagram"`) for additional variants.

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Orchestration | LangChain |
| LLM | Google Gemini (`gemini-1.5-flash`) |
| API Framework | FastAPI |
| Validation | Pydantic |
| Frontend | Plain HTML/CSS/JS (no framework) |

---

##  Why This Design

Most simple AI integrations are a single prompt-in, text-out call. This project demonstrates an **agentic pattern**: independent agents with distinct responsibilities (planning, writing, critiquing) that pass structured state between them, with a self-correction step before the user ever sees the output — the same architectural pattern used in the author's larger [AI Research Agent](https://github.com/bilalrafique5/AI-Research-agent) project, scaled down into a fast, focused mini-agent.

---

##  Author

Built by [Bilal Rafique](https://github.com/bilalrafique5).