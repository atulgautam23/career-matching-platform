from services.skill_matching import calculate_skill_match


def analyze_student_skills(
    student_skills: list[str],
    required_skills: list[str]
) -> dict:

    result = calculate_skill_match(
        student_skills=student_skills,
        required_skills=required_skills
    )

    return {
        "match_percentage": result["match_percentage"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"]
    }