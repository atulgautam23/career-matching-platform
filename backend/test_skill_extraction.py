import asyncio

from services.skill_extraction import extract_skills


async def main():
    job_description = """
    We are looking for a Data Analyst proficient in Python,
    SQL, Excel, Power BI and Pandas.
    """

    skills = await extract_skills(job_description)

    print("Extracted skills:")
    print(skills)


asyncio.run(main())