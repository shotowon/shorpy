from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from shorpy.models.base import Base


class URL(Base):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(primary_key=True)
    alias: Mapped[str] = mapped_column(String(length=6), unique=True)
    url: Mapped[str] = mapped_column(String())
