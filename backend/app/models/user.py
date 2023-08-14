import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Role(str, Enum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())

    email: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    password_hash: Mapped[str] = mapped_column(String(256))
    role: Mapped[Role] = mapped_column(default=Role.DEFAULT)

    active: Mapped[bool] = mapped_column(default=False)
    activated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    department_id: Mapped[UUID] = mapped_column(ForeignKey("departments.id"), nullable=True)
