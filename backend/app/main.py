from fastapi import FastAPI
from app.routers.test_router import router as test_router
from app.routers.patients import router as patients_router

app = FastAPI(title="React Chatbot")

app.include_router(patients_router)