from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import Role


class UserAccountSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    role: Role
    department_code: Optional[str]
    active: bool
    activated_at: Optional[datetime]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AccountActivationRequestSchema(BaseModel):
    email: EmailStr


class CreateDepartmentSchema(BaseModel):
    name: str = Field(..., min_length=6, max_length=128)
    code: str = Field(..., max_length=8, min_length=3, pattern=r"^[A-Za-z]*$")
    description: str


class UpdateDepartmentSchema(BaseModel):
    name: str = Field(..., max_length=128)
    description: str

    model_config = ConfigDict(from_attributes=True)
