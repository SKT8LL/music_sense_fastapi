import time
import uuid
from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas import PredictRequest, PredictResponse
from settings import settings

router = APIRouter(prefix="/api/v1", tags=["predict"])


def _dummy_inference(features: List[float]) -> List[float]:
    return [0.0 for _ in range(64)]


@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    start = time.perf_counter()

    if len(payload.features) != 128:
        raise HTTPException(status_code=400, detail="features must have length 128")

    output = _dummy_inference(payload.features)
    latency_ms = (time.perf_counter() - start) * 1000

    return {
        "request_id": str(uuid.uuid4()),
        "haptic_vector": output,
        "latency_ms": latency_ms,
        "model_version": settings.MODEL_VERSION,
    }
