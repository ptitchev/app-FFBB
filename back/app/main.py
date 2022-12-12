from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta, date

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

def get_match(db: Session, date: date):
    """
    Recupere les matchs dans la base de donnée en fonction du jour
    """
    return db.query(models.Match).filter(models.Match.jour > date - timedelta(days=15), models.Match.jour < date + timedelta(days=15)).all()


@app.get("/api/request_get", response_model=schemas.Match)
async def send_to_front(date: date, db: Session = Depends(get_db)):
    matchByDate = get_match(db, date)
    return matchByDate


@app.post("/api/request_post", response_model=schemas.Match)
async def send_to_front(date: request.MatchRequest, db: Session = Depends(get_db)):
    matchByDate = await get_match(db, date.date)
    return matchByDate
