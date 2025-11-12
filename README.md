# secure-user-api

# Secure User API

FastAPI-based secure user authentication system with JWT tokens and SQLite database.

## Features
- User Registration
- User Login (JWT)
- Protected Route `/me`
- Password Hashing (bcrypt)
- SQLAlchemy ORM + Alembic migrations

## Getting Started
1. Create virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `uvicorn app.main:app --reload`
