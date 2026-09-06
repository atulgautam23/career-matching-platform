# import httpx

# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     adzuna_app_id: str
#     adzuna_app_key: str

#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )


# settings = Settings()


# async def search_jobs(
#     job_role: str,
#     location: str = "India",
#     results_per_page: int = 10
# ) -> list:

#     url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

#     params = {
#         "app_id": settings.adzuna_app_id,
#         "app_key": settings.adzuna_app_key,
#         "results_per_page": results_per_page,
#         "what": job_role,
#         "where": location,
#         "content-type": "application/json"
#     }

#     async with httpx.AsyncClient(timeout=20.0) as client:
#         response = await client.get(
#             url,
#             params=params
#         )

#     response.raise_for_status()

#     data = response.json()

#     jobs = []

#     for job in data.get("results", []):
#         jobs.append({
#             "external_job_id": job.get("id"),
#             "title": job.get("title"),
#             "company": job.get("company", {}).get("display_name"),
#             "description": job.get("description"),
#             "location": job.get("location", {}).get("display_name"),
#             "created": job.get("created"),
#             "apply_url": job.get("redirect_url")
#         })

#     return jobs
import httpx

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    adzuna_app_id: str
    adzuna_app_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()


async def search_jobs(
    job_role: str,
    location: str = "India",
    results_per_page: int = 3,
    page: int = 1
) -> list:

    url = (
        f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"
    )

    params = {
        "app_id": settings.adzuna_app_id,
        "app_key": settings.adzuna_app_key,
        "results_per_page": results_per_page,
        "what": job_role,
        "where": location,
        "content-type": "application/json"
    }

    async with httpx.AsyncClient(timeout=20.0) as client:

        response = await client.get(
            url,
            params=params
        )

    response.raise_for_status()

    data = response.json()

    jobs = []

    for job in data.get("results", []):

        jobs.append({
            "external_job_id": job.get("id"),
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "description": job.get("description"),
            "location": job.get("location", {}).get("display_name"),
            "created": job.get("created"),
            "apply_url": job.get("redirect_url")
        })

    return jobs