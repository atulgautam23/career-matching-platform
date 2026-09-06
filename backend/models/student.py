from pydantic import BaseModel, Field
from typing import List


class Education(BaseModel):
    degree: str
    institution: str
    graduation_year: int = Field(ge=1900, le=2100)


class Project(BaseModel):
    title: str
    description: str
    technologies: List[str] = []


class Certification(BaseModel):
    name: str
    issuing_organization: str
    year: int = Field(ge=1900, le=2100)


class StudentProfile(BaseModel):
    name: str
    email: str
    education: List[Education]
    skills: List[str]
    certifications: List[Certification] = []
    projects: List[Project] = []
    target_job_role: str