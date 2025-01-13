from fastapi import APIRouter

from shorpy.api.v1.url import router as url_router

router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(url_router)
