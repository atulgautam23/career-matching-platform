# from fastapi import APIRouter, HTTPException
# from models.student import StudentProfile
# from database.database import db
# from services.student_analysis import analyze_student_skills
# from uuid import uuid4
# import re


# router = APIRouter(prefix="/students", tags=["Students"])


# @router.post("/profile")
# async def create_student_profile(profile: StudentProfile):
#     student_id = str(uuid4())

#     try:
#         student_data = profile.model_dump()
#         student_data["student_id"] = student_id

#         db.students.insert_one(student_data)

#         return {
#             "message": "Student profile created successfully",
#             "student_id": student_id
#         }

#     except Exception as e:
#      print(f"Student profile error: {e}")

#     raise HTTPException(
#         status_code=500,
#         detail="Failed to create student profile"
#     )


# @router.get("/{student_id}/analysis")
# async def analyze_student(student_id: str):

#     student = db.students.find_one({
#         "student_id": student_id
#     })

#     if not student:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )

#     target_role = student["target_job_role"]

#     try:
#         # Find jobs matching the student's target role
#         jobs = db.jobs.find({
#             "title": {
#                 "$regex": f"^{re.escape(target_role)}$",
#                 "$options": "i"
#             }
#         })

#         # Collect required skills from matching jobs
#         required_skills = set()

#         for job in jobs:
#             for skill in job.get("required_skills", []):
#                 required_skills.add(skill)

#         required_skills = sorted(required_skills)

#         # Analyze student's skills against required skills
#         analysis = analyze_student_skills(
#             student_skills=student.get("skills", []),
#             required_skills=required_skills
#         )

#         return {
#             "student_id": student_id,
#             "target_job_role": target_role,
#             "current_skills": student.get("skills", []),
#             "required_skills": required_skills,
#             **analysis
#         }

#     except Exception as e:
#         print(f"Student analysis error: {e}")

#         raise HTTPException(
#             status_code=500,
#             detail="Failed to analyze student skills"
#         )
from fastapi import APIRouter, HTTPException

from models.student import StudentProfile
from database.database import db
from services.student_analysis import analyze_student_skills

from uuid import uuid4
import re


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# =========================
# CREATE STUDENT PROFILE
# =========================

@router.post("/profile")
async def create_student_profile(profile: StudentProfile):

    student_id = str(uuid4())

    student_data = profile.model_dump()

    student_data["student_id"] = student_id

    db.students.insert_one(student_data)

    return {
        "message": "Student profile created successfully",
        "student_id": student_id
    }


# =========================
# STUDENT SKILL ANALYSIS
# =========================

@router.get("/{student_id}/analysis")
async def analyze_student(student_id: str):

    student = db.students.find_one({
        "student_id": student_id
    })

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    target_role = student["target_job_role"]

    try:

        # Find jobs matching the student's target role
        jobs = db.jobs.find({
            "title": {
                "$regex": f"^{re.escape(target_role)}$",
                "$options": "i"
            }
        })

        # Collect required skills from matching jobs
        required_skills = set()

        for job in jobs:

            for skill in job.get(
                "required_skills",
                []
            ):

                required_skills.add(skill)

        required_skills = sorted(
            required_skills
        )

        # Analyze student's skills
        analysis = analyze_student_skills(
            student_skills=student.get(
                "skills",
                []
            ),
            required_skills=required_skills
        )

        return {
            "student_id": student_id,

            "target_job_role": target_role,

            "current_skills":
                student.get(
                    "skills",
                    []
                ),

            "required_skills":
                required_skills,

            **analysis
        }

    except Exception as e:

        print(
            f"Student analysis error: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to analyze student skills"
        )