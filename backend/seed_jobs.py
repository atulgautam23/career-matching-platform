from database.database import db
from uuid import uuid4


jobs = [
    {
        "title": "Data Scientist",
        "company": "CareerMatch",
        "description": "Data Scientist role requiring Python, SQL, Pandas, NumPy, Statistics, Machine Learning and Data Visualization.",
        "required_skills": [
            "python",
            "sql",
            "pandas",
            "numpy",
            "statistics",
            "machine learning",
            "data visualization"
        ]
    },

    {
        "title": "Software Engineer",
        "company": "CareerMatch",
        "description": "Software Engineer role requiring programming, data structures and algorithms, object oriented programming, Git, SQL and problem solving.",
        "required_skills": [
            "python",
            "java",
            "data structures",
            "algorithms",
            "object oriented programming",
            "git",
            "sql",
            "problem solving"
        ]
    },

    {
        "title": "Frontend Developer",
        "company": "CareerMatch",
        "description": "Frontend Developer role requiring HTML, CSS, JavaScript, React, Git and responsive web development.",
        "required_skills": [
            "html",
            "css",
            "javascript",
            "react",
            "git",
            "responsive web development"
        ]
    },

    {
        "title": "Backend Developer",
        "company": "CareerMatch",
        "description": "Backend Developer role requiring Python, FastAPI, REST APIs, SQL, MongoDB, Git and API development.",
        "required_skills": [
            "python",
            "fastapi",
            "rest api",
            "sql",
            "mongodb",
            "git",
            "api development"
        ]
    },

    {
        "title": "Machine Learning Engineer",
        "company": "CareerMatch",
        "description": "Machine Learning Engineer role requiring Python, NumPy, Pandas, Scikit-learn, Machine Learning, Deep Learning, Git and SQL.",
        "required_skills": [
            "python",
            "numpy",
            "pandas",
            "scikit-learn",
            "machine learning",
            "deep learning",
            "git",
            "sql"
        ]
    }
]


for job in jobs:

    existing_job = db.jobs.find_one({
        "title": job["title"]
    })

    if existing_job:
        print(f"{job['title']} already exists. Skipping.")
        continue

    job["job_id"] = str(uuid4())

    db.jobs.insert_one(job)

    print(f"{job['title']} added successfully.")


print("Job seeding completed.")