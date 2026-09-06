# # from services.job_search import search_jobs
# # from services.skill_extraction import extract_skills
# # from services.skill_matching import calculate_skill_match


# # MIN_MATCH_PERCENTAGE = 0.0


# # async def recommend_jobs(
# #     student_skills: list[str],
# #     target_job_role: str,
# #     location: str = "India",
# #     limit: int = 10
# # ) -> list:

# #     # Search for jobs matching the student's target role
# #     jobs = await search_jobs(
# #         job_role=target_job_role,
# #         location=location,
# #         results_per_page=limit
# #     )

# #     recommended_jobs = []

# #     for job in jobs:
# #         description = job.get("description") or ""

# #         # Extract required skills from the job description
# #         required_skills = await extract_skills(description)

# #         # Calculate student's match with this job
# #         match_result = calculate_skill_match(
# #             student_skills=student_skills,
# #             required_skills=required_skills
# #         )

# #         # Recommend only jobs meeting the minimum threshold
# #         if match_result["match_percentage"] < MIN_MATCH_PERCENTAGE:
# #             continue

# #         recommended_jobs.append({
# #             "external_job_id": job.get("external_job_id"),
# #             "title": job.get("title"),
# #             "company": job.get("company"),
# #             "location": job.get("location"),
# #             "created": job.get("created"),
# #             "apply_url": job.get("apply_url"),
# #             "required_skills": required_skills,
# #             "match_percentage": match_result["match_percentage"],
# #             "matched_skills": match_result["matched_skills"],
# #             "missing_skills": match_result["missing_skills"]
# #         })

# #     # Highest matching jobs first
# #     recommended_jobs.sort(
# #         key=lambda job: job["match_percentage"],
# #         reverse=True
# #     )

# #     return recommended_jobs
# from services.job_search import search_jobs
# from services.skill_extraction import extract_skills
# from services.skill_matching import calculate_skill_match


# MIN_MATCH_PERCENTAGE = 0.0


# async def recommend_jobs(
#     student_skills: list[str],
#     target_job_role: str,
#     location: str = "India",
#     limit: int = 10
# ) -> list:

#     jobs = await search_jobs(
#         job_role=target_job_role,
#         location=location,
#         results_per_page=limit
#     )

#     recommended_jobs = []


#     for job in jobs:

#         description = job.get("description") or ""


#         # Try AI skill extraction
#         try:

#             required_skills = await extract_skills(
#                 description
#             )

#         except Exception as e:

#             print(
#                 f"Skill extraction failed for "
#                 f"{job.get('title')}: {e}"
#             )

#             # If Gemini is unavailable,
#             # still show the job.
#             required_skills = []


#         match_result = calculate_skill_match(
#             student_skills=student_skills,
#             required_skills=required_skills
#         )


#         if match_result["match_percentage"] < MIN_MATCH_PERCENTAGE:
#             continue


#         recommended_jobs.append({

#             "external_job_id":
#                 job.get("external_job_id"),

#             "title":
#                 job.get("title"),

#             "company":
#                 job.get("company"),

#             "location":
#                 job.get("location"),

#             "created":
#                 job.get("created"),

#             "apply_url":
#                 job.get("apply_url"),

#             "required_skills":
#                 required_skills,

#             "match_percentage":
#                 match_result["match_percentage"],

#             "matched_skills":
#                 match_result["matched_skills"],

#             "missing_skills":
#                 match_result["missing_skills"]

#         })


#     recommended_jobs.sort(
#         key=lambda job: job["match_percentage"],
#         reverse=True
#     )


#     return recommended_jobs

from services.job_search import search_jobs
from services.skill_extraction import extract_skills
from services.skill_matching import calculate_skill_match


MIN_MATCH_PERCENTAGE = 0.0


async def recommend_jobs(
    student_skills: list[str],
    target_job_role: str,
    location: str = "India",
    limit: int = 3,
    page: int = 1
) -> list:

    jobs = await search_jobs(
        job_role=target_job_role,
        location=location,
        results_per_page=limit,
        page=page
    )

    recommended_jobs = []


    for job in jobs:

        description = job.get("description") or ""


        # Try AI skill extraction
        try:

            required_skills = await extract_skills(
                description
            )

        except Exception as e:

            print(
                f"Skill extraction failed for "
                f"{job.get('title')}: {e}"
            )

            # Still show the job if Gemini is unavailable
            required_skills = []


        # Calculate skill match
        match_result = calculate_skill_match(
            student_skills=student_skills,
            required_skills=required_skills
        )


        if match_result["match_percentage"] < MIN_MATCH_PERCENTAGE:
            continue


        recommended_jobs.append({

            "external_job_id":
                job.get("external_job_id"),

            "title":
                job.get("title"),

            "company":
                job.get("company"),

            "location":
                job.get("location"),

            "created":
                job.get("created"),

            "apply_url":
                job.get("apply_url"),

            "required_skills":
                required_skills,

            "match_percentage":
                match_result["match_percentage"],

            "matched_skills":
                match_result["matched_skills"],

            "missing_skills":
                match_result["missing_skills"]

        })


    # Highest match first
    recommended_jobs.sort(
        key=lambda job: job["match_percentage"],
        reverse=True
    )


    return recommended_jobs