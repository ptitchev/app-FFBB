from datetime import datetime, date
from pydantic import BaseModel


class MatchRequest(BaseModel):
    date: date
    lat: float
    lng: float
