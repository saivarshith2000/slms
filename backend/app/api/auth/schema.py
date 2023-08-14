from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import Role


class BaseUserSchema(BaseModel):
    email: EmailStr
    first_name: str = Field(..., max_length=64)
    last_name: str = Field(..., max_length=64)
    role: Role = Field(...)

    model_config = ConfigDict(from_attributes=True)


class CreateUserSchema(BaseUserSchema):
    password: str = Field(..., max_length=64, min_length=8)
