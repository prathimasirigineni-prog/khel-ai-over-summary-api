from fastapi import FastAPI, HTTPException

from schemas import OverSummaryResponse
from services import get_over_summary


app = FastAPI(
    title="Khel AI - Over Summary API",
    description="API for retrieving over-by-over cricket summaries.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Khel AI Over Summary API is running"
    }


@app.get(
    "/innings/{innings_id}/overs",
    response_model=list[OverSummaryResponse]
)
def over_summary(innings_id: int):
    summary = get_over_summary(innings_id)

    if summary is None:
        raise HTTPException(
            status_code=404,
            detail="Innings not found"
        )

    return summary