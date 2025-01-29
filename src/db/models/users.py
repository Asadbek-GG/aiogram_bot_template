from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import mapped_column, Mapped
from src.db.models.base import TimeBaseModel




class User(TimeBaseModel):
    # class Type(Enum):
    #     USER = "user"
    #     ADMIN = "admin"
    #     SUPER_ADMIN = "super_admin"

    first_name: Mapped[str] = mapped_column(VARCHAR(255))
    last_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    # type: # Mapped[Type] = mapped_column(SQLEnum(Type), default=Type.USER)
