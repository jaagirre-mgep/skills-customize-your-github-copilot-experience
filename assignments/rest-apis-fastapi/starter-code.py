from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(
    title="Student Management API",
    description="A REST API for managing student records",
    version="1.0.0"
)

# Define the Student model


class Student(BaseModel):
    """Student data model"""
    student_id: int
    name: str
    email: str
    grade: str

    class Config:
        schema_extra = {
            "example": {
                "student_id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "grade": "A"
            }
        }


# In-memory database (for demonstration)
students_db: List[Student] = []


# TODO: Implement GET /students endpoint to retrieve all students


# TODO: Implement GET /students/{student_id} endpoint to retrieve a single student


# TODO: Implement POST /students endpoint to create a new student


# TODO: Implement PUT /students/{student_id} endpoint to update a student


# TODO: Implement DELETE /students/{student_id} endpoint to delete a student


# TODO: Add filtering, sorting, and pagination features


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
