from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.schemas import HealthResponse

router = APIRouter(prefix="/api/v1", tags=["health"])


@router.get("/healthz", response_model=HealthResponse)
def health_check(request: Request, db: Session = Depends(get_db)):
    # 1. Check Database
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        # Log error here in real app
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed",
        )

    # 2. Check ONNX Model
    if not hasattr(request.app.state, "onnx_session"):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model state uninitialized",
        )

    return {"status": "ok"}
