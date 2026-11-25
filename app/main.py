import asyncio
import sys

# Playwright on Windows requires ProactorEventLoop for subprocess support
# Okay this doesn't do shit ignore it
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models import Snapshot  # noqa: F401
from app.routers import snapshot


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Link Archiving Service API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(snapshot.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}