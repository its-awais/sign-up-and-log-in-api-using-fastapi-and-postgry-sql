# Sign Up and Log In API

A FastAPI-based authentication API with PostgreSQL database integration.

## Prerequisites

- Python 3.9+
- PostgreSQL
- pgAdmin4 (optional, for database management)

## Setup Instructions

### 1. Initialize the Project with UV

First, install UV if you haven't already:

```bash
pip install uv
```

Then initialize the project:

```bash
uv init
```

### 2. Install Dependencies

Install all required packages using UV:

```bash
uv add fastapi pydantic pydantic-settings uvicorn sqlalchemy argon2-cffi email-validator python-dotenv asyncpg
```

### 3. Set Up the Database

1. Install and run PostgreSQL
2. Create a new database in pgAdmin4
3. Update your environment variables with the database connection details

### 4. Run the Application

Start the development server:

```bash
uv run main.py
```

The API will be available at `http://localhost:8000`

## Project Structure

- **main.py** - Application entry point (runs uvicorn)
- **app.py** - FastAPI application setup
- **config.py** - Configuration settings
- **core/** - Core functionality including database lifespan and security
- **models/** - Database models (User table)
- **Schema/** - Pydantic schemas for request/response validation
- **Router/** - API route handlers (sign up, log in)
- **database.py** - Database connection and session management

## Dependencies

- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI web server
- **SQLAlchemy** - ORM
- **asyncpg** - Async PostgreSQL driver
- **Argon2** - Password hashing
- **Email-validator** - Email validation
- **python-dotenv** - Environment variable management

## Features

- User registration (sign up)
- User authentication (log in)
- Secure password hashing with Argon2
- Email validation
- Email verification (sign-up sends a verification link; user must verify before logging in)

## Configuration / Environment Variables

This project uses `pydantic-settings` and reads variables from a `.env` file.
Make sure the following are set before running the app:

- `DATABASE_URL` (PostgreSQL connection URL)
- `SECRET_KEY` (JWT signing key)
- `ALGORITHM` (JWT signing algorithm, e.g. `HS256`)
- `ACCESS_TOKEN_EXPIRE_MINUTES` (token expiration time)
- `BASE_URL` (public base URL for verification links, e.g. `http://localhost:8000`)
- `MAIL_USERNAME` (SMTP username)
- `MAIL_PASSWORD` (SMTP password or app password)

## alembic migration

- When you change the database schema (add/remove columns), run:
  ```bash
  alembic revision --autogenerate -m "add user table"
  ```

- Then apply changes:
  ```bash
  alembic upgrade head
  ```


## License

MIT
