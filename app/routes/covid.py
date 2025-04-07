from fastapi import APIRouter, Query
from typing import Optional
from app.db import get_db_connection

router = APIRouter()

@router.get("/api/v1/covid/cases")
def get_covid_cases(state: str, start: Optional[str] = None, end: Optional[str] = None):
    conn = get_db_connection()
    cur = conn.cursor()

    query = "SELECT state, date, cases, deaths FROM covid_data WHERE state = %s"
    params = [state.upper()]

    if start:
        query += " AND date >= %s"
        params.append(start)
    if end:
        query += " AND date <= %s"
        params.append(end)

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {
            "state": r[0],
            "date": r[1].isoformat(),
            "cases": r[2],
            "deaths": r[3]
        } for r in rows
    ]
