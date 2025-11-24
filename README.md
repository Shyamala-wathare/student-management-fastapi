🎓 Student Management System (FastAPI + MySQL)

A backend application that manages students, courses, and marks, built using FastAPI and MySQL.
Includes JWT authentication, CRUD APIs, and interactive Swagger documentation.

⭐ Features

🔐 User Signup & Login using JWT

👨‍🎓 Create, update, delete, list students

📚 Manage courses with fees, duration & credits

📝 Add and update student marks

🗄️ MySQL database storage

⚡ FastAPI with auto-generated API docs


🛠 Tech Stack

FastAPI

Python

MySQL

SQLAlchemy

PyJWT

bcrypt

Uvicorn


🔗 API Highlights
Authentication

POST /auth/signup – Register

POST /auth/login – Login (returns JWT token)

Students

POST /students/

GET /students/

PUT /students/{id}

DELETE /students/{id}

Courses

POST /courses/courses/

GET /courses/courses/

Marks

POST /marks/

GET /marks/


🚀 How to Run

Install dependencies

pip install -r requirements.txt


Start FastAPI

uvicorn main:app --reload


Open API docs
👉 http://127.0.0.1:8000/docs


📌 Usage

Signup → Login → Copy token

Click Authorize in Swagger

Paste:Bearer <your_token>

Now all protected routes will work.
