from fastapi import FastAPI
from app.routers.patients import router as patients_router

app = FastAPI(title="CareFlow AI")

app.include_router(patients_router)