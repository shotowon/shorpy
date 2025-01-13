from pydantic import BaseModel, HttpUrl


class SaveURL(BaseModel):
    url: HttpUrl
    alias: str | None = None
