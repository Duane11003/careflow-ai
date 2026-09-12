from fastapi import FastAPI
from app.routers.test_router import router as test_router

app = FastAPI(title="React Chatbot")

app.include_router(test_router)