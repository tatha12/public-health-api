
# 🩺 Public Health API

A production-ready backend project for delivering real-time, filterable public health data via a RESTful API.  
This API currently focuses on **COVID-19 case data** across U.S. states, backed by live ingestion from trusted sources like the New York Times.

> ✅ Built with FastAPI, PostgreSQL, AWS (EC2 + RDS), and deployed using NGINX + Gunicorn  
> ✅ Designed for real-world applications and research/policy integrations

---

## 🚀 Features

- ✅ Query COVID-19 case and death data by state and date range
- ✅ Real-time ETL pipeline using NYTimes public datasets
- ✅ Cloud-hosted backend (FastAPI + PostgreSQL on AWS)
- ✅ RESTful API with OpenAPI docs (`/docs`)
- ✅ NGINX reverse proxy for production deployment
- ✅ SSL-secured PostgreSQL connection (via RDS)
- 🔄 Extensible design (more datasets coming soon: air quality, hospitals, etc.)

---

## 🧰 Tech Stack

| Layer        | Tech            |
|--------------|-----------------|
| API          | FastAPI         |
| Language     | Python 3.12     |
| Database     | PostgreSQL (RDS)|
| Deployment   | AWS EC2 + NGINX |
| Data Source  | NYTimes COVID-19|
| ETL Script   | Python + Pandas |
| CI/CD        | GitHub Actions (coming soon) |

---

## 📁 Project Structure

```
public-health-api/
├── app/
│   ├── main.py               # FastAPI entry point
│   ├── db.py                 # DB connection setup
│   └── routes/
│       └── covid.py          # COVID API endpoints
├── scripts/
│   └── load_covid_data.py    # ETL script for COVID data
├── .env                      # DB credentials (not committed)
├── .gitignore
├── requirements.txt
├── README.md
```

---

## 🧪 Setup Instructions (Local / EC2)

```bash
# Clone the repo
git clone git@github.com:tatha12/public-health-api.git
cd public-health-api

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env  # Fill in DB_HOST, USER, PASS, etc.

# Run app locally
uvicorn app.main:app --reload
```

Then visit:  
➡️ `http://localhost:8000/docs` to use the API.

---

## ⚙️ API Endpoints

| Method | URL |
|--------|-----|
| `GET`  | `/api/v1/covid/cases?state=MA&start=2020-01-01&end=2020-06-01` |
| `GET`  | `/db-status` – Test DB connection |
| `GET`  | `/` – Root health check |

---

## 📊 ETL Script: Load COVID-19 Data

Pulls live COVID-19 data from the NYTimes GitHub CSV and loads it into the `covid_data` table in PostgreSQL (RDS).

### Run it manually:

```bash
python scripts/load_covid_data.py
```

> Downloads 1M+ rows and safely inserts into RDS.

---

## ☁️ Deployment Overview (AWS)

- ✅ Deployed to AWS EC2 (Ubuntu 24.04)
- ✅ PostgreSQL hosted on AWS RDS (with SSL)
- ✅ nginx configured as reverse proxy on port 80
- ✅ FastAPI app served via `gunicorn`
- ✅ Environment secrets stored in `.env`

**Next Goals:**
- GitHub Actions for CI/CD pipeline
- Docker container for portable deployment
- Add background scheduler to auto-refresh data weekly

---

## 📘 Example Use Case

This project is suitable for:

- Research groups and policy analysts monitoring public health trends
- Backend developer portfolio projects
- NIW/EB1 evidence showing national interest or data transparency work
- Open data advocates and public dashboards

---

## ✍️ Author

**Tathagata Goswami**  
Full-stack + Backend Engineer | Data-Focused Projects | FastAPI + AWS | Public Data

GitHub: [@tatha12](https://github.com/tatha12)

---

## 📌 License

MIT License – free to use and build on. Data is sourced from the [NYTimes COVID-19 dataset](https://github.com/nytimes/covid-19-data).
