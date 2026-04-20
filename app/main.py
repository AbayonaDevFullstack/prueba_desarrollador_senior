from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Task Manager API", lifespan=lifespan)
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
