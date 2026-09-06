from fastapi import APIRouter, HTTPException

from database.database import db
from services.skill_matching import calculate_skill_match


router = APIRouter(prefix="/matching", tags=["Matching"])


@router.get("/student/{student_id}/job/{job_id}")
async def match_student_with_job(
    student_id: str,
    job_id: str
):
    student = db.students.find_one({
        "student_id": student_id
    })

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    job = db.jobs.find_one({
        "job_id": job_id
    })

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    result = calculate_skill_match(
        student_skills=student.get("skills", []),
        required_skills=job.get("required_skills", [])
    )

    return {
        "student_id": student_id,
        "job_id": job_id,
        "job_title": job["title"],
        "company": job["company"],
        **result
    }


@router.get("/student/{student_id}/job/{job_id}/recommendations")
async def get_skill_recommendations(
    student_id: str,
    job_id: str
):
    student = db.students.find_one({
        "student_id": student_id
    })

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    job = db.jobs.find_one({
        "job_id": job_id
    })

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    result = calculate_skill_match(
        student_skills=student.get("skills", []),
        required_skills=job.get("required_skills", [])
    )

    recommendations = [
        {
            "skill": skill,
            "reason": f"Required for the {job['title']} role"
        }
        for skill in result["missing_skills"]
    ]

    return {
        "student_id": student_id,
        "job_id": job_id,
        "job_title": job["title"],
        "match_percentage": result["match_percentage"],
        "missing_skills": result["missing_skills"],
        "recommendations": recommendations
    }