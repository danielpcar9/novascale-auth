from sqlmodel import SQLModel, Field as SQLField, AutoString
from pydantic import field_validator
from typing import Annotated
from pydantic import Field as PyField

# Common types/validators can be shared or duplicated if they apply to both
NameString = Annotated[str, PyField(min_length=1, max_length=100)]

class User(SQLModel, table=True):
    id: int | None = SQLField(default=None, primary_key=True)
    name: NameString
    email: str = SQLField(sa_type=AutoString, index=True, unique=True)
    age: int = PyField(ge=0, le=120)
    username: str = SQLField(min_length=5, index=True, unique=True)
    hashed_password: str = SQLField()

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
