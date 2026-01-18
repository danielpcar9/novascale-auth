from sqlmodel import SQLModel, Field as SQLField, AutoString
from pydantic import Field as PyField, field_validator
from typing import Annotated, Optional

# Here we use PyField because Annotated is for Pydantic types
NameString = Annotated[str, PyField(min_length=1, max_length=100)]


class UserBase(SQLModel):
    name: NameString
    email: str = SQLField(sa_type=AutoString, index=True, unique=True)
    age: int = PyField(ge=0, le=120)
    username: str = SQLField(min_length=5, index=True, unique=True)

    @field_validator("name")
    @classmethod
    def name_must_be_alphabetic(cls, v: str) -> str:
        cleaned_name = v.strip()
        if not all(part.isalpha() for part in cleaned_name.split()):
            raise ValueError("Name must have alphabetical characters and spaces")
        return cleaned_name.title()

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        v = v.strip().lower()
        if "admin" in v:
            raise ValueError("For safety username cannot contain the word 'admin'")
        return v


class User(UserBase, table=True):
    id: Optional[int] = SQLField(default=None, primary_key=True)
    hashed_password: str = SQLField()


class UserCreate(UserBase):
    password: str = PyField(min_length=8)


class UserRead(UserBase):
    id: int


class Token(SQLModel):
    access_token: str
    token_type: str


if __name__ == "__main__":
    try:
        # Successful test with everything combined
        user = User(
            name="  ana garcía  ",
            email="ANA@example.com",
            age=30,
            username="  AnaDev2026  ",
        )
        print("✅ ALL GOOD:")
        print(f"Name: {user.name}")  # Ana García
        print(f"Username: {user.username}")  # anadev2026

    except Exception as e:
        print(f"❌ Validation error:\n{e}")
