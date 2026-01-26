# Sign-Up and Log-In API using FastAPI & PostgreSQL

A simple, fast, and secure **Sign-Up and Log-In API** built using **FastAPI** and **PostgreSQL**, featuring async database operations, password hashing, and validation.

---

## Features

- User Sign-Up
- Email uniqueness check
- Password hashing with **Argon2**
- Async database operations with SQLAlchemy & asyncpg
- Pydantic data validation (name, email, password)
- Ready for JWT authentication extension
- Modular folder structure for scalability

---

## Folder Structure

backend/
├── app/
│ ├── Router/ # API routes (sign-up, login)
│ ├── Schema/ # Pydantic schemas
│ ├── models/ # Database tables
│ ├── core/ # Lifespan & utilities
│ └── app.py # App entry point
├── main.py # Uvicorn entry point
├── .gitignore
├── pyproject.toml
├── README.md
└── config.py # Configuration settings

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/its-awais/sign-up-and-log-in-api-using-fastapi-and-postgry-sql.git
cd sign-up-and-log-in-api-using-fastapi-and-postgry-sql/backend
