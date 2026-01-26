from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from sqlalchemy.orm  import DeclarativeBase
from config import setting

class Base(DeclarativeBase):
    pass


engine = create_async_engine(setting.DATABASE_URL,echo= setting.DEBUG)
session_maker = async_sessionmaker(engine, expire_on_commit=False)



async def get_async_session() -> AsyncGenerator[AsyncSession,None]:
    async with session_maker() as session:
           yield session