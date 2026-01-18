# 🔐 NovaScale Auth

An authentication microservice with anomaly detection.
Designed to be **scalable, secure, and deployable**.

## 🚀 Features

- Registration and login with JWT (JSON Web Tokens).
- Robust data validation with Pydantic and SQLModel.
- Integrated anomaly detection (ML-ready architecture).
- Automated testing with Pytest.
- Modern dependency management with `uv`.

## 🛠️ Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL (SQLModel)
- **Security**: Passlib (bcrypt), PyJWT
- **Testing**: Pytest
- **Tooling**: `uv`, Ruff
- **Language**: Python 3.14+

## 📦 Requirements

- Python 3.14+
- `uv` (https://github.com/astral-sh/uv)
- PostgreSQL (local or remote)

## ▶️ Getting Started Locally

```bash
# 1. Clone the repository
git clone https://github.com/danielpcar9/novascale-auth.git
cd novascale-auth

# 2. Create virtual environment and install dependencies
uv sync

# 3. Configure environment variables (Optional for now)
# The service uses a default DATABASE_URL in app/database.py

# 4. Run the application
uv run uvicorn app.main:app --reload
```

## 🧪 Testing

To run automated tests:

```bash
export PYTHONPATH=$PYTHONPATH:.
pytest
```

## 🏗️ Project Structure

- `app/api/`: API endpoints (v1).
- `app/models/`: Data models and schemas definition.
- `app/services/`: Business logic and authentication.
- `app/ml/`: Machine Learning components (anomaly detection).
- `tests/`: Unit and integration tests.
