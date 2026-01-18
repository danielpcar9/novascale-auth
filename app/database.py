# app/database.py
"""Database configuration and session management."""

from sqlmodel import create_engine, Session


DATABASE_URL = "postgresql+psycopg://user:password@localhost:5432/novascale"

engine = create_engine(DATABASE_URL)

def get_session() -> Session:
    """Provide a synchronous database session."""
    with Session(engine) as session:
        yield session