from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.config import settings

engine = create_async_engine(str(settings.db_connection_string), future=True, echo=True)

session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def pg_context(app: web.Application):
    async with session_maker() as session:
        app["db"] = session
        yield
        await app["db"].close()


__all__ = ["engine", "pg_context"]
