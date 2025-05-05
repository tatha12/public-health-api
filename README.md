# Public Health Dashboard

This project is a full-stack web application that allows users to search and view public health data such as COVID-19 case numbers and air quality index (AQI) levels. It is built using FastAPI for the backend and React with TailwindCSS for the frontend.

## Features

- Search COVID-19 cases by US state and date range
- Upload and query local air quality data
- Frontend and backend hosted on AWS EC2 with nginx
- PostgreSQL database hosted on AWS RDS
- Secure CI/CD using GitHub Actions and SSH
- Built with testing and deployment reliability in mind

## Tech Stack

**Backend:**
- Python, FastAPI
- PostgreSQL
- SQLAlchemy, psycopg2

**Frontend:**
- React, Vite
- TailwindCSS

**Infrastructure:**
- AWS EC2 (Ubuntu)
- AWS RDS (PostgreSQL)
- nginx
- GitHub Actions for CI/CD

## Getting Started

### Backend (FastAPI)

```bash
cd public-health-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (React)

```bash
cd public-health-frontend
npm install
npm run dev
```

## Deployment

The app is deployed on an Ubuntu EC2 instance using nginx to serve the React frontend and reverse proxy to the FastAPI backend. Database is hosted on RDS.

## Future Improvements

- Add automated testing
- Add CI/CD health checks
- Add documentation for API endpoints

## Author

Tathagata Goswami
