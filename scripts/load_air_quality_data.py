# scripts/load_air_quality_data.py

import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

CSV_PATH = "data/sample_air_quality_data.csv"

def main():
    print("Loading air quality data...")
    df = pd.read_csv(CSV_PATH)

    # Connect to the database
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode="require"
    )
    cur = conn.cursor()

    inserted = 0
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO air_quality (state, date, aqi_value, aqi_category, pollutant)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (row["state"], row["date"], row["aqi_value"], row["aqi_category"], row["pollutant"]))
        inserted += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"✅ Inserted {inserted} rows.")

if __name__ == "__main__":
    main()
