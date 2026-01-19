import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"  # Default to SQLite for now, override in prod
    MODEL_PATH: str = os.path.join(os.path.dirname(__file__), "model.onnx")
    ENV: str = "dev"
    
    class Config:
        env_file = ".env"

settings = Settings()
