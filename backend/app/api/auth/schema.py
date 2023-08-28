import re
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

from app.models.user import Role


class BaseUserSchema(BaseModel):
    email: EmailStr
    first_name: str = Field(..., max_length=64)
    last_name: str = Field(..., max_length=64)
    role: Role = Field(...)
    department_code: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def validate_department_code(self):
        if not self.department_code:
            return self
        if self.role == Role.ADMIN:
            return self
        if 3 <= len(self.department_code) <= 8 and re.match("^[A-Za-z]*$", self.department_code):
            return self
        raise ValueError("Department code must be between 3 and 8 characters for Non-Administrator users")


class CreateUserSchema(BaseUserSchema):
    password: str = Field(..., max_length=64, min_length=8)


class SignInResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: BaseUserSchema
