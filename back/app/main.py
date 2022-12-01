from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from .models import models
from .database import SessionLocal
from .schemas import request, schemas


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="App_ffbb",
    description="My description",
    version="0.0.1",
    docs_url="/doc", redoc_url="/redoc", openapi_url="/openapi.json"
)

origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/day", tags=["Dates"])
def get_day_of_week():
    """
    Get the current day of week
    """
    return datetime.now().strftime("%A")


@app.post("/api/request", response_model=list[schemas.Match])
async def send_to_front(match_request: request.MatchRequest, db = Depends(get_db)):
    # req_match = await match_request.json()
    return db.query(models.Match).filter(models.Match.jour > match_request.date - timedelta(days=1), models.Match.jour < match_request.date + timedelta(days=1)).all()
