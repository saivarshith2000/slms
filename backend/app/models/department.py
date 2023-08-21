import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(128))
    code: Mapped[str] = mapped_column(String(8), unique=True, index=True)
    description: Mapped[str] = mapped_column(Text())

    users: Mapped[List["User"]] = relationship()
