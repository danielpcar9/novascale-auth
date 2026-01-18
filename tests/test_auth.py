import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.main import app
from app.database import get_session

# Setup in-memory database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

def override_get_session():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)

def setup_module(module):
    SQLModel.metadata.create_all(engine)

def test_register_user():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 25,
            "username": "testuser",
            "password": "password123"
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "password" not in data
    assert "hashed_password" not in data

def test_register_duplicate_username():
    client.post(
        "/api/v1/auth/register",
        json={
            "name": "Another User",
            "email": "another@example.com",
            "age": 30,
            "username": "duplicateuser",
            "password": "password123"
        },
    )
    response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Duplicate User",
            "email": "different@example.com",
            "age": 30,
            "username": "duplicateuser",
            "password": "password123"
        },
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "User with this username or email already exists"

def test_login_success():
    # Register first
    client.post(
        "/api/v1/auth/register",
        json={
            "name": "Login User",
            "email": "login@example.com",
            "age": 22,
            "username": "loginuser",
            "password": "secretpassword"
        },
    )
    
    # Try login
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "loginuser", "password": "secretpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_fail():
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "loginuser", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"
