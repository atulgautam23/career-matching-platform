from pydantic import BaseModel, Field
from typing import List


class Job(BaseModel):
    title: str
    company: str
    description: str
    required_skills: List[str] = Field(default_factory=list)
    location: str | None = None
    employment_type: str | None = None
    source: str | None = None
    apply_url: str | None = None