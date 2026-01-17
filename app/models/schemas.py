from sqlmodel import SQLModel, Field as SQLField, AutoString
from pydantic import Field as PyField, field_validator
from typing import Annotated, Optional

# Aquí usamos PyField porque Annotated es para tipos de Pydantic
NameString = Annotated[str, PyField(min_length=1, max_length=100)]


class User(SQLModel, table=True):
    id: Optional[int] = SQLField(default=None, primary_key=True)

    name: NameString
    # Usamos SQLField para que SQLModel sepa cómo guardarlo en DB
    email: str = SQLField(sa_type=AutoString, index=True, unique=True)


    age: int = PyField(ge=0, le=120)

    # Aquí también, usa SQLField para definir el comportamiento en DB
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



if __name__ == "__main__":
    try:
        # Prueba exitosa con todo combinado
        user = User(
            name="  ana garcía  ",
            email="ANA@example.com",
            age=30,
            username="  AnaDev2026  ",
        )
        print("✅ TODO PERFECTO:")
        print(f"Nombre: {user.name}")  # Ana García
        print(f"Username: {user.username}")  # anadev2026

    except Exception as e:
        print(f"❌ Error de validación:\n{e}")
