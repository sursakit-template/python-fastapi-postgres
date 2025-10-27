from fastapi import FastAPI
from app.routers import users
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI User CRUD API", version="1.0.0")

# Include routers
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "FastAPI User CRUD API"}

