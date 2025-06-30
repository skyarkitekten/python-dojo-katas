from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os
from pathlib import Path

class Settings(BaseSettings):
    openai_api_key: Optional[str] = None
    model_name: Optional[str] = None
    system_prompt: Optional[str] = None
    # temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    # max_tokens: int = Field(default=150, ge=1, le=4096)
    # top_p: float = Field(default=1.0, ge=0.0, le=1.0)
    # frequency_penalty: float = Field(default=0.0, ge=0.0, le=2.0)
    # presence_penalty: float = Field(default=0.0, ge=0.0, le=2.0)

    class Config:
        env_file = Path(__file__).resolve().parent.parent.parent.parent / ".env"
        env_file_encoding = "utf-8"

settings = Settings()
