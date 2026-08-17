# AP CSA Practice Platform

Interactive web app for AP Computer Science A practice:
- MCQ from past exams (College Board 2019+)
- FRQ with auto-grader
- (Phase 2) Per-topic accuracy tracking
- (Phase 3) Personalized recommendations

## Status
🚧 Phase 1 — scaffolding

## Tech Stack
- **Backend**: Python 3.12, FastAPI, SQLModel, PostgreSQL 16
- **Frontend**: TypeScript, React 18, Vite, TanStack Query, Tailwind CSS
- **Infra**: Docker Compose (local Postgres)

## Project Layout
- `backend/` — FastAPI app
- `frontend/` — Vite + React app
- `data/` — Seed data (questions, fixtures)

## Quick Start
~~~bash
# 1. 起数据库
docker compose up -d db

# 2. 起后端(终端 2)
cd backend && uv sync && uv run uvicorn app.main:app --reload

# 3. 起前端(终端 3)
cd frontend && npm install && npm run dev

# 4. 浏览器访问
# 前端:http://localhost:5173
# 后端文档:http://localhost:8000/docs
~~~

## Roadmap
- [x] Phase 1.1: Scaffolding
- [ ] Phase 1.2: Minimal DB + seed MCQ
- [ ] Phase 1.3: MCQ practice UI
- [ ] Phase 1.4: FRQ autograder (local subprocess)
- [ ] Phase 1.5: Demo + README polish
