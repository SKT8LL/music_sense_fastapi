from pydantic import BaseModel, Field
from typing import List


class PredictRequest(BaseModel):
    audio_data: List[float]
    sample_rate: int = Field(..., gt=0)


class PredictResponse(BaseModel):
    haptic_pattern: List[List[float]]
    inference_time: float


class HealthResponse(BaseModel):
    status: str


class MetaResponse(BaseModel):
    model_version: str
    input_shape: List[str]
