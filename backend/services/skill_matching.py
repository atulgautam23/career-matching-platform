from typing import List


# Common alternative names for the same skill
SKILL_ALIASES = {
    "excel": "microsoft excel",
    "ms excel": "microsoft excel",
    "microsoft excel": "microsoft excel",

    "powerbi": "power bi",
    "power bi": "power bi",
    "microsoft power bi": "power bi",

    "py": "python",

    "postgres": "postgresql",
    "postgres sql": "postgresql",

    "js": "javascript",
    "node": "node.js",
    "nodejs": "node.js",

    "reactjs": "react",
    "react.js": "react",

    "ml": "machine learning",
    "ai": "artificial intelligence",
}


def normalize_skill(skill: str) -> str:
    """
    Convert a skill into a consistent canonical form.
    """
    skill = " ".join(skill.strip().lower().split())

    return SKILL_ALIASES.get(skill, skill)


def calculate_skill_match(
    student_skills: List[str],
    required_skills: List[str]
) -> dict:

    student_set = {
        normalize_skill(skill)
        for skill in student_skills
        if skill.strip()
    }

    required_set = {
        normalize_skill(skill)
        for skill in required_skills
        if skill.strip()
    }

    if not required_set:
        return {
            "match_percentage": 0.0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched = student_set.intersection(required_set)
    missing = required_set - student_set

    match_percentage = (
        len(matched) / len(required_set)
    ) * 100

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }