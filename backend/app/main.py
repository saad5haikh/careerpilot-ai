
from fastapi import FastAPI

app = FastAPI(
    title="CareerPilot AI",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "app": "CareerPilot AI",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
@app.post("/career-advice")
def career_advice():
    return {
            "job_match": 92,
                    "recommended_roles": [
                                "Corporate Sales Manager",
                                            "Business Development Manager",
                                                        "Training Manager"
                                                                ],
                                                                        "message": "Based on your profile, you are highly suitable for leadership and commercial roles."
                                                                            }
                                                                            from pydantic import BaseModel

                                                                            class ResumeRequest(BaseModel):
                                                                                resume_text: str

                                                                                @app.post("/analyze-resume")
                                                                                def analyze_resume(request: ResumeRequest):
                                                                                    return {
                                                                                            "skills": [
                                                                                                        "Sales",
                                                                                                                    "Business Development",
                                                                                                                                "Training",
                                                                                                                                            "Customer Service"
                                                                                                                                                    ],
                                                                                                                                                            "experience_level": "Senior",
                                                                                                                                                                    "recommended_jobs": [
                                                                                                                                                                                "Corporate Sales Manager",
                                                                                                                                                                                            "Training Manager",
                                                                                                                                                                                                        "Business Development Manager"
                                                                                                                                                                                                                ],
                                                                                                                                                                                                                        "estimated_salary": {
                                                                                                                                                                                                                                    "minimum": 3000,
                                                                                                                                                                                                                                                "maximum": 8000,
                                                                                                                                                                                                                                                            "currency": "USD"
                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                        