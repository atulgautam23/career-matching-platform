from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import client
from routes.students import router as student_router
from routes.jobs import router as job_router
from routes.matching import router as matching_router


app = FastAPI(
    title="Career Matching Platform API",
    version="1.0.0",
    description="API for student skill analysis and job matching."
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(student_router)
app.include_router(job_router)
app.include_router(matching_router)


@app.get("/health")
async def health_check():

    try:

        client.admin.command("ping")

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:

        return {
            "status": "unhealthy",
            "database": "disconnected"
        }