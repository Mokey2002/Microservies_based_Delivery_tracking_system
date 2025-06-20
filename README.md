
# Microservices Demo Project with FastAPI

This project is a simple microservices-based architecture implemented using FastAPI. It demonstrates the creation and interaction of separate services for handling users, orders, and tracking, each with its own SQLite database and API.

## Services Overview

### 1. User Service
- Handles user creation and retrieval.
- Runs on port `8001`.

### 2. Order Service
- Handles creation and listing of orders.
- Depends on the User Service for user verification.
- Runs on port `8002`.

### 3. Tracking Service
- Handles tracking orders.
- Depends on the Order Service to associate tracking info with orders.
- Runs on port `8003`.

## Project Structure

```
microservices/
│
├── user/               # User service (FastAPI)
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── Dockerfile
│
├── Order/              # Order service (FastAPI)
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── Dockerfile
│
├── tracking/           # Tracking service (FastAPI)
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

## How to Run

Make sure Docker and Docker Compose are installed.

```bash
# Build and run all services
docker compose up --build
```

Visit:
- `http://localhost:8001/docs` - User Service
- `http://localhost:8002/docs` - Order Service
- `http://localhost:8003/docs` - Tracking Service

## Technologies Used

- FastAPI
- SQLite
- Docker
- Docker Compose
- Pydantic
- SQLAlchemy

## License

MIT

