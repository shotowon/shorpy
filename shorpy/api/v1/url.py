from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import APIRouter, Response, Depends, status

from shorpy.gears.random import string as rnd_str
from shorpy.api.dependencies import get_db_session
from shorpy.schemes.url import SaveURL
import shorpy.crud.url as url_crud

router = APIRouter(prefix="/url", tags=["url"])


@router.get("/{alias}")
async def redirect(
    alias: str,
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> Response:
    url = await url_crud.get_url_by_alias(session=session, alias=alias)
    if url:
        return RedirectResponse(
            url.url,
            status_code=status.HTTP_302_FOUND,
        )

    return JSONResponse(
        content={"error": "url for given alias not given"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@router.post("/")
async def save(
    url: SaveURL,
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> Response:
    alias = url.alias
    if alias is None:
        alias = rnd_str.new_random_string(6)

    try:
        new_alias = await url_crud.save_url(
            session=session, alias=alias, url=str(url.url)
        )

        return JSONResponse(
            content={"message": f"new url with alias {new_alias} was added"},
            status_code=status.HTTP_200_OK,
        )
    except IntegrityError:
        session.rollback()
        return JSONResponse(
            content={
                "message": f"url with alias {alias} already exists, use other alias"
            },
            status_code=status.HTTP_409_CONFLICT,
        )
    except Exception:
        session.rollback()
        return JSONResponse(
            content={"message": "internal error"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
