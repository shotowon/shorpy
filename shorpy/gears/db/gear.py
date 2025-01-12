from typing import AsyncContextManager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)


class DBGear:
    def __init__(self, url: str, echo: bool = False, echo_pool: bool = False):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
        )

        self.session_maker: async_sessionmaker[AsyncSession] = (
            async_sessionmaker(
                bind=self.engine,
                autoflush=False,
                autocommit=False,
                expire_on_commit=False,
            )
        )

    def get_session(self) -> AsyncContextManager[AsyncSession]:
        return self.session_maker()

    async def dispose(self) -> None:
        await self.engine.dispose()
