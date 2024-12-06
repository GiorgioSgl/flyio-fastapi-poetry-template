import sys

from fastapi import FastAPI
from .routers import users

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}