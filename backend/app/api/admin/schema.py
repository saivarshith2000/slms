from pydantic import BaseModel, ConfigDict, EmailStr, Field


class AccountActivationRequestSchema(BaseModel):
    email: EmailStr


class UpdateDepartmentSchema(BaseModel):
    name: str = Field(..., max_length=128)
    description: str

    model_config = ConfigDict(from_attributes=True)
