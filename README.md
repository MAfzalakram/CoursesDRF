# 📘 Course Management API

A RESTful API built using **Django** and **Django REST Framework (DRF)** that allows you to create, read, update, and delete course records. This project is ideal for learning backend API development and can serve as a base for building educational platforms.

---

## 🚀 Features

- ✅ Create a new course  
- 📋 View a list of all courses  
- 🔍 Retrieve course details by ID  
- ✏️ Update course information  
- ❌ Delete a course  
- 📄 Swagger/OpenAPI Documentation included  

---

## 🛠 Tech Stack

- Python 3.x  
- Django 5.x  
- Django REST Framework  
- SQLite (default, can be swapped for PostgreSQL)  
- DRF Browsable API  
- Swagger (drf-yasg)  

---

## 📁 API Endpoints

| Method | Endpoint                  | Description                    |
|--------|---------------------------|--------------------------------|
| GET    | `/api/courses/`           | List all courses               |
| POST   | `/api/courses/`           | Create a new course            |
| GET    | `/api/courses/<id>/`      | Retrieve a course by ID        |
| PUT    | `/api/courses/<id>/`      | Update an entire course        |
| PATCH  | `/api/courses/<id>/`      | Partially update a course      |
| DELETE | `/api/courses/<id>/`      | Delete a course by ID          |

---

## 🧪 Example JSON (Course Creation)

```json
{
  "course_name": "Python for Beginners",
  "instructor": "John Doe",
  "description": "An introductory course on Python.",
  "duration_weeks": 6,
  "price": "250.00"
}