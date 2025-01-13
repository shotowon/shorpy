from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from shorpy.models import URL


async def get_url_by_alias(session: AsyncSession, alias: str) -> URL | None:
    stmt = select(URL).filter(URL.alias == alias)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def save_url(session: AsyncSession, alias: str, url: str) -> str | None:
    new_url = URL(alias=alias, url=url)
    try:
        session.add(new_url)
        await session.flush()
        await session.commit()
        return new_url.alias
    except IntegrityError as e:
        await session.rollback()
        raise e
