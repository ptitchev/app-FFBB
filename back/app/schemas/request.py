from datetime import datetime
from pydantic import BaseModel


class MatchRequest(BaseModel):
    date: datetime
    lat: float
    lng: float
