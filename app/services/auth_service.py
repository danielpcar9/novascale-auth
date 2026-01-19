# app/services/auth_service.py
"""Authentication service with JWT and password hashing."""

import logfire
from datetime import datetime, timedelta, timezone
from typing import Any, TypeVar

from jose import jwt
from passlib.context import CryptContext
from sqlmodel import Session, select

from app.models.orm import User
from app.models.schemas import UserCreate

T = TypeVar("T")

SECRET_KEY = "your-very-long-and-secure-secret-key-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """Handles user authentication and token generation."""

    def __init__(self, detector: Any):
        self.detector = detector

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed one."""
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        """Generate password hash."""
        with logfire.span("hashing password"):
            return pwd_context.hash(password)

    def create_user(self, *, user_create: UserCreate, session: Session) -> User:
        """Create a new user in the database."""
        db_user = User(
            name=user_create.name,
            email=user_create.email,
            age=user_create.age,
            username=user_create.username,
            hashed_password=self.get_password_hash(user_create.password),
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    def authenticate(
        self, *, username: str, password: str, session: Session
    ) -> User | None:
        """Authenticate user by username and password."""
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()

        if not user:
            return None
        if not self.verify_password(
            password, user.hashed_password
        ):  # assuming this field exists
            return None

        # Optional: anomaly check
        # if self.detector.is_anomaly(...):
        #     raise ValueError("Suspicious activity detected")

        return user

    def create_access_token(
        self, data: dict, expires_delta: timedelta | None = None
    ) -> str:
        """Create JWT access token."""
        to_encode = data.copy()
        expire = (
            datetime.now(timezone.utc) + expires_delta
            if expires_delta
            else datetime.now(timezone.utc)
            + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
