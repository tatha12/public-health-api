from fastapi import APIRouter, Query
from typing import Optional
from app.db import get_db_connection

router = APIRouter()

@router.get("/api/v1/air-quality")
def get_air_quality(
    state: str = Query(..., description="State 2-letter code (e.g. CA, NY)"),
    date: Optional[str] = Query(None, description="Date in YYYY-MM-DD format")
):
    conn = get_db_connection()
    cur = conn.cursor()

    query = "SELECT state, date, aqi_value, aqi_category, pollutant FROM air_quality WHERE state = %s"
    params = [state.upper()]

    if date:
        query += " AND date = %s"
        params.append(date)

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {
            "state": r[0],
            "date": r[1].isoformat(),
            "aqi_value": r[2],
            "aqi_category": r[3],
            "pollutant": r[4]
        } for r in rows
    ]
