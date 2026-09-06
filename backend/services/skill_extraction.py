from google import genai
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gemini_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


class SkillExtractionResult(BaseModel):
    skills: list[str]


settings = Settings()

client = genai.Client(
    api_key=settings.gemini_api_key
)


async def extract_skills(job_description: str) -> list[str]:
    prompt = f"""
Extract the technical and professional skills required for this job.

Rules:
- Extract only skills explicitly required or clearly relevant to the job.
- Normalize skill names.
- Remove duplicate skills.
- Do not invent skills.
- Return the result using the provided JSON schema.

Job description:
{job_description}
"""

    interaction = await client.aio.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": SkillExtractionResult.model_json_schema()
        }
    )

    result = SkillExtractionResult.model_validate_json(
        interaction.output_text
    )

    return result.skills