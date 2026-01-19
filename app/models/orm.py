from sqlmodel import SQLModel, Field as SQLField, AutoString

class User(SQLModel, table=True):
    id: int | None = SQLField(default=None, primary_key=True)
    name: str = SQLField(max_length=100)
    email: str = SQLField(sa_type=AutoString, index=True, unique=True)
    age: int = SQLField()
    username: str = SQLField(min_length=5, index=True, unique=True)
    hashed_password: str = SQLField()
