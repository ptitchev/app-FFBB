from datetime import datetime
from pydantic import BaseModel


class MatchRequest(BaseModel):
    localisation: str
    date: datetime
