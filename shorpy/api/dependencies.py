from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from shorpy.core.app import db_gear


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in db_gear.get_session():
        yield session
