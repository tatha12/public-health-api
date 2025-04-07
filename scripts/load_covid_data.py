# scripts/load_covid_data.py

import os
import requests
import pandas as pd
import psycopg2
from io import StringIO
from dotenv import load_dotenv

# Load DB credentials
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# NYTimes CSV URL (state-level COVID cases and deaths)
CSV_URL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

# Mapping full state names to their 2-letter codes
STATE_CODES = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

def main():
    # Download the CSV
    print("Downloading COVID data...")
    response = requests.get(CSV_URL)
    response.raise_for_status()  # raise exception if download fails

    # Read CSV into DataFrame
    df = pd.read_csv(StringIO(response.text))
    print(f"Downloaded {len(df)} rows")

    # Transform: keep relevant columns and convert state names to codes
    df['state'] = df['state'].map(STATE_CODES)
    df = df.dropna(subset=['state'])  # remove any unrecognized states
    df = df[['state', 'date', 'cases', 'deaths']]

    # Insert into DB
    print("Connecting to DB...")
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
        user=DB_USER, password=DB_PASSWORD, sslmode="require"
    )
    cur = conn.cursor()

    inserted = 0
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO covid_data (state, date, cases, deaths)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (row['state'], row['date'], int(row['cases']), int(row['deaths'])))
        inserted += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"✅ Inserted {inserted} records into covid_data")

if __name__ == "__main__":
    main()
