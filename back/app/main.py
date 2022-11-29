from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from .schemas import MatchRequest
# from .. import Auth


app = FastAPI(
    title="App_ffbb",
    description="My description",
    version="0.0.1",
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

@app.post("/api/request")
async def send_to_front(matchRequest : MatchRequest):
    return ""

