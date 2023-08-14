from pydantic import BaseModel, ConfigDict, Field


class DepartmentSchema(BaseModel):
    name: str = Field(..., max_length=128)
    abbreviation: str = Field(..., max_length=8, min_length=3, pattern=r"^[A-Za-z]*$")
    description: str

    model_config = ConfigDict(from_attributes=True)
