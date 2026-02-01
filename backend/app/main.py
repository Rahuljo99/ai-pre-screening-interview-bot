from backend.app.api.resume import router as resume_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(resume_router, prefix="/resume", tags=["resume"])