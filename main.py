from fastapi import FastAPI
from routes import student_routes

app = FastAPI()

app.include_router(student_routes.router, prefix="/students", tags=["students"])
