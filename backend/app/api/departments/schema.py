from pydantic import BaseModel, ConfigDict, Field


class DepartmentSchema(BaseModel):
    name: str = Field(..., max_length=128)
    code: str = Field(...)
    description: str

    model_config = ConfigDict(from_attributes=True)


class DepartmentDetailSchema(BaseModel):
    name: str = Field(...)
    code: str = Field(...)
    description: str = Field(...)
    course_count: int = 0
    student_count: int = 0

    model_config = ConfigDict(from_attributes=True)
