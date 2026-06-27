from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

@app.get("/")
def root():
  return {"message" : "Welcome to Workforce Management System API"}  

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/version")
def version():
    return {
        "version": settings.app_version
    }

from app.db.database import engine

@app.get("/database")
def database():
    return {
        "message": "Database connection created successfully"
    }