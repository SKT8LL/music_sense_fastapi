from fastapi import APIRouter
from app.schemas import MetaResponse

router = APIRouter(prefix="/api/v1", tags=["meta"])


@router.get("/meta", response_model=MetaResponse)
def get_model_metadata():
    # TODO: Fetch this from actual loaded ONNX session or config
    return {"model_version": "v1.0.0", "input_shape": ["1", "128"]}
