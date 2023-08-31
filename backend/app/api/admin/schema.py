from pydantic import BaseModel, ConfigDict, EmailStr, Field


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
