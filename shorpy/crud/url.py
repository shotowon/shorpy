from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shorpy.models import URL


async def get_url_by_alias(session: AsyncSession, alias: str) -> URL | None:
    stmt = select(URL).filter(URL.alias == alias)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
