from typing import List

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    onnx_providers: List[str]
    model_loaded: bool
    database_ok: bool
    timestamp: str


class MetaResponse(BaseModel):
    model_name: str
    version: str
    input_shape: List[int]
    output_shape: List[int]
    dtype: str
    latency_target_ms: int


class PredictRequest(BaseModel):
    features: List[float] = Field(..., min_length=128, max_length=128)
    batch_size: int = Field(1, ge=1, le=32)


class PredictResponse(BaseModel):
    request_id: str
    haptic_vector: List[float] = Field(..., min_length=64, max_length=64)
    latency_ms: float
    model_version: str
