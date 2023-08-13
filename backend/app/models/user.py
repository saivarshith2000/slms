import uuid
from enum import Enum
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from .base import Base
from .department import Department


class Role(str, Enum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()
    )

    email: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    password_hash: Mapped[str] = mapped_column(String(256))
    role: Mapped[Role] = mapped_column(default=Role.DEFAULT)

    active: Mapped[bool] = mapped_column(default=False)
    activated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.id"), nullable=True
    )
