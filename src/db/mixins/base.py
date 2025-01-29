import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, declared_attr, mapped_column





class TimeStampMixin(object):
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )


class TableNameMixin(object):

    @declared_attr
    def __tablename__(cls) -> str:
        if cls.__name__.endswith("s"):
            return cls.__name__.lower() + "es"
        else:
            return cls.__name__.lower() + "s"


class BaseModelMixin(TimeStampMixin, TableNameMixin):
    __table_args__ = {"extend_existing": True}
    __mapper_args__ = {"always_refresh": True}
    id: Mapped[int] = mapped_column(primary_key=True)
