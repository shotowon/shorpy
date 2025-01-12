from typing import Literal
from pathlib import Path
from typing import Tuple
import argparse
import json
import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    BaseModel,
    Field,
    PostgresDsn,
    ValidationError,
)

from shorpy import BASE_DIR

Env = Literal["local", "dev", "prod"]


class PostgresSettings(BaseModel):
    dsn: PostgresDsn = Field(alias="dsn")


class HttpServerSettings(BaseModel):
    port: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="shorpy_")

    env: Env = Field(alias="env")
    postgres: PostgresSettings = Field(alias="postgres")
    http_server: HttpServerSettings = Field(alias="http_server")


def load() -> Tuple[Settings, Exception]:
    arg_parser = argparse.ArgumentParser(
        "shorpy",
        "run this REST API in the background",
        "Simple URL Shortener REST API",
    )

    arg_parser.add_argument("-c", "--config")
    args = arg_parser.parse_args()
    configPath = args.config

    if configPath is None:
        configPath = os.getenv("SHORPY_CONFIG_PATH")

    if configPath is None:
        return (
            None,
            Exception("error: config unspecified"),
        )

    try:
        with open(configPath) as f:
            configData = json.load(f)

    except FileNotFoundError as e:
        return (
            None,
            Exception("error: config file does not exist"),
        )
    except json.decoder.JSONDecodeError:
        return (
            None,
            Exception("error: invalid json"),
        )

    try:
        settings: Settings = Settings(**configData)
        return (
            settings,
            None,
        )
    except ValidationError as e:
        return (
            None,
            e,
        )
