from fastapi import FastAPI
from app.routes import covid, air_quality

from app.db import get_db_connection

app = FastAPI()

app.include_router(covid.router)
app.include_router(air_quality.router)

@app.get("/")
def read_root():
    return {"message": "Public Health API is up and running!"}

@app.get("/db-status")
def db_status():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return {"status": "connected", "db_version": version}
    except Exception as e:
        return {"status": "error", "details": str(e)}
