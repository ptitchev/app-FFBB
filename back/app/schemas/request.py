from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated

class MatchRequest(BaseModel):
    localisation: str
    date: datetime