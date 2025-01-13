from contextlib import asynccontextmanager
import logging
import asyncio

from sqlalchemy import text
from fastapi import FastAPI
import uvicorn

from shorpy.core.app import cfg, db_gear
from shorpy.api.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_gear.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)


def main():
    logger = logging.getLogger("main")
    logger.info(f"starting FastAPI server on port {cfg.http_server.port}")
    uvicorn.run("shorpy.main:app", host="0.0.0.0", port=cfg.http_server.port)


if __name__ == "__main__":
    main()
