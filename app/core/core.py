from contextlib import asynccontextmanager
from app.database import Base,engine
from app.models.User import User
@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield