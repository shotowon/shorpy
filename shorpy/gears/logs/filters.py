import logging
from typing import override
from logging import Filter, LogRecord

from shorpy.gears.config.config import Env


class NoErrors(Filter):
    @override
    def filter(self, record: LogRecord) -> bool | LogRecord:
        return record.levelno < logging.WARNING


class Env(Filter):
    def __init__(self, env: Env) -> None:
        self._env = env

    @override
    def filter(self, record: LogRecord) -> bool | LogRecord:
        record.env = self._env
        return True
