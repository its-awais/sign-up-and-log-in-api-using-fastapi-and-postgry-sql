from contextlib import asynccontextmanager
from app.database import Base,engine

@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)
        yield