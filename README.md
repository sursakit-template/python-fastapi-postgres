# FastAPI User CRUD API

A simple REST API built with FastAPI to perform CRUD operations on User entities.

## Features

- ✅ CRUD operations for Users
- ✅ PostgreSQL with SQLAlchemy ORM
- ✅ Pydantic validation
- ✅ Unique constraints on email and phone
- ✅ Standard HTTP status codes

## Tech Stack

- FastAPI (Python 3.9+)
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn



## Quick Start

### 1. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API available at `http://localhost:8000`

### 2. Set Up Database


CREATE DATABASE fastapi_db;


### 3. Configure Environment
 

Edit `.env` with your database credentials:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
```
 
## Project Structure

```
python-fastapi-postgres/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   └── routers/
│       └── users.py     # User endpoints
├── requirements.txt
├── .env.example
└── README.md
```
