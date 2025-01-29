from enum import Enum
from typing import Optional

from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import mapped_column, Mapped

from src.db.models.base import TimeBaseModel


class User(TimeBaseModel):
    class Type(Enum):
        USER = "user"
        ADMIN = "admin"
        SUPER_ADMIN = "superuser"

    first_name: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(VARCHAR(100), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(VARCHAR(100), nullable=True)
    username: Mapped[Optional[str]] = mapped_column(VARCHAR(100), nullable=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    type: Mapped[Type] = mapped_column(SQLEnum(Type), default=Type.USER)
