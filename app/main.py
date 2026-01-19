import logfire
import logging
from rich.logging import RichHandler
from rich.console import Console
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.auth import router as auth_router  # Import your router

# Setup rich console
console = Console()

# Setup logging with Rich
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger("rich")

@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    console.print("[bold green]NovaScale Auth API is starting up...[/bold green] 🚀")
    logger.info("Application startup complete.")
    yield
    # Shutdown
    console.print("[bold red]NovaScale Auth API is shutting down...[/bold red] 👋")

app = FastAPI(title="NovaScale Auth API", lifespan=lifespan)

logfire.configure(send_to_logfire=False)
logfire.instrument_fastapi(app)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/", tags=["health"])
def root():
    return {"message": "Auth Service active"}
