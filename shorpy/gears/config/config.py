from typing import Literal
from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic import (
    BaseModel,
    Field,
    PostgresDsn,
    ValidationError,
)

from shorpy import BASE_DIR


class PostgresSettings(BaseModel):
    dsn: PostgresDsn = Field(alias="dsn")


class HttpServerSettings(BaseModel):
    port: int


class Settings(BaseSettings):
    env: Literal["local", "dev", "prod"]
    postgres: PostgresSettings = Field(alias="postgres")
    http_server: HttpServerSettings = Field(alias="http_server")
