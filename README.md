# Chatbot
This is a chatbot application with a React frontend and a Python backend. The backend is hitting OpenAI's API directly. LangChain is planned for future iterations.

## Stack

**Frontend**: React
**Backend**: Python (FastAPI)

## Prerequisites
- Node.js and npm
- Python 3.13 and 'uv'
- An OpenAI API key

## Setup
- Create a .env file in the backend root directory and add a OPENAI_API_KEY variable

## Running Locally
Backend - ```uv run fastai dev```
Frontend - ```npm run dev```

## Roadmap
Migrate direct OpenAI calls to LangChain