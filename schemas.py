from pydantic import BaseModel
from typing import List


class BallSummary(BaseModel):
    over_ball: str
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