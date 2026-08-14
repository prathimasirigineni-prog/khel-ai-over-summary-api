from pydantic import BaseModel
from typing import List, Optional


class BallEvent(BaseModel):
    over_ball: str
    striker: str
    bowler: str
    runs: int
    extras: int = 0
    is_legal: bool = True
    extra_type: Optional[str] = None
    wicket: bool = False
    label: str


class OverSummaryRequest(BaseModel):
    innings_id: int
    ball_events: List[BallEvent]


class BallSummary(BaseModel):
    over_ball: str
    striker: str
    bowler: str
    runs: int
    extras: int
    wicket: bool
    label: str


class OverSummaryResponse(BaseModel):
    over_number: int
    runs: int
    wickets: int
    extras: int
    balls: List[BallSummary]