import uuid
from datetime import date, datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .department import Department


class CourseTeacherRole(str, Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"


class CourseApplicationStatus(str, Enum):
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"


class CourseTeacher(Base):
    __tablename__ = "course_teacher"

    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    course_code: Mapped[UUID] = mapped_column(ForeignKey("courses.code"), primary_key=True)
    role: Mapped[CourseTeacherRole] = mapped_column(nullable=False)


class CourseStudent(Base):
    __tablename__ = "course_student"

    student_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    course_code: Mapped[UUID] = mapped_column(ForeignKey("courses.code"), primary_key=True)
    application_status: Mapped[CourseApplicationStatus] = mapped_column(
        nullable=False, default=CourseApplicationStatus.PENDING
    )
    application_note: Mapped[str]
    grade: Mapped[float] = mapped_column(default=0.0)


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    code: Mapped[str] = mapped_column(String(8), unique=True, index=True, nullable=False)
    credits: Mapped[int] = mapped_column(nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    start_date: Mapped[date] = mapped_column(Date(), nullable=False)
    end_date: Mapped[date] = mapped_column(Date(), nullable=False)

    active: Mapped[bool] = mapped_column(default=False)
    activated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    department_code: Mapped[UUID] = mapped_column(ForeignKey("departments.code"), nullable=False)
    department: Mapped["Department"] = relationship(back_populates="courses")
