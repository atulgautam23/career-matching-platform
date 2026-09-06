# from fastapi import APIRouter, HTTPException
# from database.database import db
# from models.job import Job
# from services.skill_extraction import extract_skills
# from services.job_search import search_jobs
# from services.job_recommendation import recommend_jobs
# from uuid import uuid4


# router = APIRouter(prefix="/jobs", tags=["Jobs"])


# @router.post("/")
# async def create_job(job: Job):
#     job_id = str(uuid4())

#     try:
#         # Extract required skills from the job description
#         extracted_skills = await extract_skills(job.description)

#         # Convert job model to dictionary
#         job_data = job.model_dump()

#         # Store AI-extracted skills
#         job_data["required_skills"] = extracted_skills
#         job_data["job_id"] = job_id

#         # Save job to MongoDB
#         db.jobs.insert_one(job_data)

#         return {
#             "message": "Job created successfully",
#             "job_id": job_id,
#             "required_skills": extracted_skills
#         }

#     except Exception as e:
#         print(f"Job creation error: {e}")

#         raise HTTPException(
#             status_code=500,
#             detail="Failed to create job"
#         )


# @router.get("/search")
# async def search_external_jobs(
#     role: str,
#     location: str = "India",
#     limit: int = 3
# ):
#     try:
#         jobs = await search_jobs(
#             job_role=role,
#             location=location,
#             results_per_page=limit
#         )

#         return {
#             "role": role,
#             "location": location,
#             "jobs": jobs
#         }

#     except Exception as e:
#         print(f"Job search error: {e}")

#         raise HTTPException(
#             status_code=502,
#             detail="Failed to fetch jobs from job search provider"
#         )


# @router.get("/recommendations/{student_id}")
# async def get_job_recommendations(
#     student_id: str,
#     location: str = "India",
#     limit: int = 10
# ):
#     student = db.students.find_one({
#         "student_id": student_id
#     })

#     if not student:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )

#     try:
#         recommendations = await recommend_jobs(
#             student_skills=student.get("skills", []),
#             target_job_role=student["target_job_role"],
#             location=location,
#             limit=limit
#         )

#         return {
#             "student_id": student_id,
#             "target_job_role": student["target_job_role"],
#             "location": location,
#             "jobs": recommendations
#         }

#     except Exception as e:
#         print(f"Job recommendation error: {e}")

#         raise HTTPException(
#             status_code=502,
#             detail="Failed to generate job recommendations"
#         )

from fastapi import APIRouter, HTTPException
from database.database import db
from models.job import Job
from services.skill_extraction import extract_skills
from services.job_search import search_jobs
from services.job_recommendation import recommend_jobs
from uuid import uuid4


router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/")
async def create_job(job: Job):
    job_id = str(uuid4())

    try:
        # Extract required skills from the job description
        extracted_skills = await extract_skills(job.description)

        # Convert job model to dictionary
        job_data = job.model_dump()

        # Store AI-extracted skills
        job_data["required_skills"] = extracted_skills
        job_data["job_id"] = job_id

        # Save job to MongoDB
        db.jobs.insert_one(job_data)

        return {
            "message": "Job created successfully",
            "job_id": job_id,
            "required_skills": extracted_skills
        }

    except Exception as e:
        print(f"Job creation error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Failed to create job"
        )


@router.get("/search")
async def search_external_jobs(
    role: str,
    location: str = "India",
    limit: int = 3,
    page: int = 1
):
    try:
        jobs = await search_jobs(
            job_role=role,
            location=location,
            results_per_page=limit,
            page=page
        )

        return {
            "role": role,
            "location": location,
            "page": page,
            "jobs": jobs
        }

    except Exception as e:
        print(f"Job search error: {e}")

        raise HTTPException(
            status_code=502,
            detail="Failed to fetch jobs from job search provider"
        )


@router.get("/recommendations/{student_id}")
async def get_job_recommendations(
    student_id: str,
    location: str = "India",
    limit: int = 3,
    page: int = 1
):
    student = db.students.find_one({
        "student_id": student_id
    })

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    try:
        recommendations = await recommend_jobs(
            student_skills=student.get("skills", []),
            target_job_role=student["target_job_role"],
            location=location,
            limit=limit,
            page=page
        )

        return {
            "student_id": student_id,
            "target_job_role": student["target_job_role"],
            "location": location,
            "page": page,
            "jobs": recommendations
        }

    except Exception as e:
        print(f"Job recommendation error: {e}")

        raise HTTPException(
            status_code=502,
            detail="Failed to generate job recommendations"
        )