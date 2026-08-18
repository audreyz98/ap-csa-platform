from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings



@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"AP CSA Backend starting (env={settings.env})")
    yield



app = FastAPI(
    title = "AP CSA Practice API",
    description = "Backend for AP Computer Science A practice platform",
    version = "0.1.0",
    lifespan = lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins_list,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)



@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}

@app.get("/")
def root():
    return {
        "name": "AP CSA Practice API",
        "version": "0.1.0",
        "docs": "/docs",
    }