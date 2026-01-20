from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.routers import health, meta, predict


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    app.state.onnx_session = None
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="FLO SENSE API", version="0.1.0", lifespan=lifespan)
    app.include_router(health.router)
    app.include_router(meta.router)
    app.include_router(predict.router)

    @app.get("/")
    def read_root():
        return {"message": "FLO SENSE API"}

    return app


app = create_app()
