import logfire
from fastapi import FastAPI
from app.api.v1.auth import router as auth_router  # Import your router

app = FastAPI(title="NovaScale Auth API")

logfire.configure(send_to_logfire=False)
logfire.instrument_fastapi(app)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/", tags=["health"])
def root():
    return {"message": "Auth Service active"}
