from fastapi import FastAPI, status
from models import User

app = FastAPI(title="NovaScale Auth API")

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: User):

    return {
        "message": "Usuario validado y registrado",
        "data": user.model_dump()
    }