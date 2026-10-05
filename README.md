# FastAPI Task CRUD

A learning project implementing a Task CRUD API using FastAPI,
PostgreSQL, SQLAlchemy, Docker Compose, and Alembic.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker Compose

## Architecture

FastAPI
↓
Pydantic
↓
SQLAlchemy
↓
PostgreSQL

Alembic manages database migrations.

## Setup

### 1. Clone repository

git clone <repository-url>

### 2. Create virtual environment

python3 -m venv venv

### 3. Activate environment

source venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure environment

cp .env.example .env

### 6. Start PostgreSQL

docker compose up -d

### 7. Run migrations

alembic upgrade head

### 8. Start FastAPI

uvicorn app.main:app --reload

## API Documentation

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| POST   | /tasks      | Create task   |
| GET    | /tasks      | Get all tasks |
| GET    | /tasks/{id} | Get task      |
| PATCH  | /tasks/{id} | Update task   |
| DELETE | /tasks/{id} | Delete task   |

## Database Migrations

Create migration:

alembic revision --autogenerate -m "description"

Apply migrations:

alembic upgrade head

Rollback:

alembic downgrade -1
