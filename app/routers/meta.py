from fastapi import APIRouter

from app.schemas import MetaResponse

router = APIRouter(prefix="/api/v1", tags=["meta"])


@router.get("/meta", response_model=MetaResponse)
def get_model_metadata():
    return {
        "model_name": "flo-sense",
        "version": "0.1.0",
        "input_shape": [1, 128],
        "output_shape": [1, 64],
        "dtype": "float32",
        "latency_target_ms": 50,
    }
