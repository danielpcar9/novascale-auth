from fastapi import FastAPI
from app.api.v1.auth import router as auth_router  # Importa tu router

app = FastAPI(title="NovaScale Auth API")

app.include_router(auth_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Servicio de Auth activo"}