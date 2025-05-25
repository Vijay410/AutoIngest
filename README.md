# AutoIngest
# 🎓 Student Info API

A modular, scalable REST API built with **FastAPI** for managing student information using PostgreSQL as the backend database. Designed using the Repository-Service pattern and fully asynchronous code for high performance and testability.

## 🚀 Features

- Clean project architecture using FastAPI
- Asynchronous endpoints
- PostgreSQL database integration
- Alembic for database migrations
- Pydantic for data validation
- Dockerized environment with Docker Compose
- pgAdmin setup for easy DB access
- Follows OOP principles with a clear separation of concerns

---

## 🧱 Tech Stack

- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **Alembic** - Database migrations
- **Pydantic** - Schema validation
- **Docker** & **Docker Compose**
- **pgAdmin** - DB UI tool

---

## 🛠️ Project Structure

app/
├── api/ # FastAPI endpoints
├── core/ # Configuration and main app
├── db/ # Database models and Alembic migration
├── repository/ # DB operations layer
├── schemas/ # Pydantic models
├── services/ # Business logic layer
├── main.py # FastAPI app entrypoint
alembic.ini # Alembic config
Dockerfile # App Dockerfile
docker-compose.yml # Compose for API + DB + pgAdmin

2️⃣ Start with Docker Compose
docker-compose up --build


API: http://localhost:8000

Docs: http://localhost:8000/v1/docs

pgAdmin: http://localhost:5050

Email: admin@example.com

Password: admin

3️⃣ Run Alembic Migrations
  -- alembic upgrade head

🔁 Upcoming Features
✅ Post API for Import student data from Excel files

✅ Patch API for Update student records using Excel

✅ Add unit tests with pytest

✅ CI/CD pipeline for deployment


🙋‍♂️ Author
Developed by Vijayvithal Kulkarni


