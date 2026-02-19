# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable and efficient REST APIs using the FastAPI framework. You'll create a production-ready API with request validation, error handling, and automatic interactive documentation while mastering asynchronous Python, data serialization, and RESTful design principles.

## 📝 Tasks

### 🛠️ Create a Student Management API

#### Description

Build a REST API for managing student records with endpoints for creating, reading, updating, and deleting student information. The API should validate incoming data, handle errors gracefully, and provide clear documentation for API consumers.

#### Requirements

Completed program should:

- Define a Student data model with appropriate fields (name, email, student_id, grade)
- Implement GET endpoint to retrieve all students
- Implement GET endpoint with path parameter to retrieve a single student by ID
- Implement POST endpoint to create a new student with request validation
- Implement PUT endpoint to update an existing student record
- Implement DELETE endpoint to remove a student by ID
- Return appropriate HTTP status codes (200, 201, 404, 422, etc.)
- Include input validation using Pydantic models
- Provide error responses with descriptive messages


### 🛠️ Add Advanced Features

#### Description

Enhance the API with filtering, sorting, and pagination capabilities. Implement features that make the API more practical for real-world usage while demonstrating advanced FastAPI concepts.

#### Requirements

Completed program should:

- Add query parameters for filtering students (by grade, name)
- Implement sorting options (by name, student ID)
- Add pagination with limit and offset parameters
- Include custom response models for different endpoints
- Implement proper exception handling with custom error messages
- Use dependency injection for shared logic where appropriate
