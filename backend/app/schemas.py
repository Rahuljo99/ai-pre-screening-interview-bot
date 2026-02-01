from pydantic import BaseModel, Field
from typing import Optional


class ExperienceSchema(BaseModel):
    company: str = Field(..., description="Name of the company")
    role: str = Field(..., description="Position held")
    start_date: str = Field(..., description="Start date of the experience")
    end_date: str = Field(..., description="End date of the experience")
    description: list[str] = Field(..., description="List of responsibilities and achievements")

class EducationSchema(BaseModel):
    institution: str = Field(..., description="Name of the educational institution")
    degree: str = Field(..., description="Degree obtained")
    field_of_study: str = Field(..., description="Field of study")
    graduation_year: int = Field(..., description="Year of graduation")

class ResumeSchema(BaseModel):
    name: str = Field(..., description="Name of the individual")
    email: str = Field(..., description="Email address of the individual")
    phone: Optional[str] = Field(None, description="Phone number of the individual")
    summary: Optional[str] = Field(None, description="Professional summary or objective")
    experience: list[ExperienceSchema] = Field(..., description="List of professional experiences")
    education: list[EducationSchema] = Field(..., description="List of educational qualifications")
    skills: list = Field(..., description="List of skills")
