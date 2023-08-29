from datetime import date, timedelta

from pydantic import BaseModel, Field, FutureDate


class CreateCourseSchema(BaseModel):
    name: str = Field(..., max_length=128)
    code: str = Field(..., max_length=16, pattern=r"^[A-Za-z]*$")
    description: str
    credits: int = Field(..., min=1)
    capacity: int = Field(..., min=1)
    start_date: date = Field(..., gt=date.today() - timedelta(days=1))
    end_date: FutureDate
    department_code: str = Field(..., max_length=16, pattern=r"^[A-Za-z]*$")


class CourseApplicationSchema(BaseModel):
    application_note: str = Field(..., max_length=128)
