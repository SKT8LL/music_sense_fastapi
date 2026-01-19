from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base
import uuid


class PredictLog(Base):
    __tablename__ = "predict_logs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    request_id = Column(String, index=True)
    input_meta = Column(Text)  # Using Text for SQLite compatibility in dev
    output_haptic = Column(Text)
    latency_ms = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ModelMetadata(Base):
    __tablename__ = "model_metadata"

    version = Column(String, primary_key=True)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Integer, default=0)
