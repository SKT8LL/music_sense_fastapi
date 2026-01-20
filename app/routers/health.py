from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import HealthResponse

router = APIRouter(prefix="/api/v1", tags=["health"])


@router.get("/healthz", response_model=HealthResponse)
def health_check(request: Request, db: Session = Depends(get_db)):
    database_ok = True
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        database_ok = False

    onnx_session = getattr(request.app.state, "onnx_session", None)
    model_loaded = onnx_session is not None
    onnx_providers: List[str] = (
        getattr(onnx_session, "providers", []) if model_loaded else []
    )

    if not database_ok or not model_loaded:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service not ready",
        )

    return {
        "status": "ok",
        "onnx_providers": onnx_providers,
        "model_loaded": model_loaded,
        "database_ok": database_ok,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
