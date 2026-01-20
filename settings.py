import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    MODEL_PATH: str = os.path.join(os.path.dirname(__file__), "model.onnx")
    MODEL_VERSION: str = "0.1.0"
    LOG_LEVEL: str = "INFO"
    ENV: str = "dev"

    class Config:
        env_file = ".env"


settings = Settings()
