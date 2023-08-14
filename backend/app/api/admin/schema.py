from pydantic import BaseModel, EmailStr, Field, ConfigDict


class AccountActivationRequestSchema(BaseModel):
    email: EmailStr
    department: str


class UpdateDepartmentSchema(BaseModel):
    name: str = Field(..., max_length=128)
    description: str

    model_config = ConfigDict(from_attributes=True)