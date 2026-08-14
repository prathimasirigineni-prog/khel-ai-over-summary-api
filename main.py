from fastapi import FastAPI, HTTPException

from schemas import (
    OverSummaryRequest,
    OverSummaryResponse,
)
from services import get_over_summary


app = FastAPI(
    title="Khel AI - Over Summary API",
    description=(
        "Integration-ready API for generating over-by-over "
        "cricket innings summaries from ball-event data."
    ),
    version="2.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Khel AI Over Summary API is running",
        "version": "2.0.0"
    }


@app.post(
    "/innings/{innings_id}/overs",
    response_model=list[OverSummaryResponse]
)
def over_summary(
    innings_id: int,
    innings_data: OverSummaryRequest
):
    if innings_data.innings_id != innings_id:
        raise HTTPException(
            status_code=400,
            detail="Innings ID does not match the supplied data"
        )

    summary = get_over_summary(innings_data)

    if summary is None:
        raise HTTPException(
            status_code=404,
            detail="No ball-event data available for this innings"
        )

    return summary