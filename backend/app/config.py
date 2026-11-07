from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if OPENAI_API_KEY is None:
    raise Exception("No open api key found")

if DATABASE_URL is None:
    raise ValueError("No DATABASE_URL found")