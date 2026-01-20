from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine, Base
from app.routers import health, meta


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables for now (naive migration)
    Base.metadata.create_all(bind=engine)
    app.state.onnx_session = None  # Placeholder for model loading
    print("Startup complete. ONNX session initialized (placeholder).")
    yield
    # Shutdown
    print("Shutdown complete.")


app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(meta.router)


@app.get("/")
def read_root():
    return {"message": "FLO SENSE API"}
