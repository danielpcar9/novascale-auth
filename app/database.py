# app/database.py
"""Database configuration and session management."""

import logfire
from typing import Generator
from sqlmodel import create_engine, Session


DATABASE_URL = "postgresql+psycopg://user:password@localhost:5432/novascale"

engine = create_engine(DATABASE_URL)
logfire.instrument_sqlalchemy(engine)


def get_session() -> Generator[Session, None, None]:
    """Provide a synchronous database session."""
    with Session(engine) as session:
        yield session