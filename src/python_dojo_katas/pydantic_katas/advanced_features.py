from pydantic import BaseModel, Field, field_validator, ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class AdvancedUserModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",  # Disallow extra fields
        str_strip_whitespace=True,  # strips whitespace from string fields
        validate_assignment=True,  # Validate on assignment
    )

    username: str = Field(..., min_length=3, max_length=50)
    email: str
    age: Optional[int] = Field(None, ge=0)

    @field_validator("email")
    @classmethod
    def email_must_be_valid(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("Invalid email address")
        return v

    @field_validator("age", mode="before")
    @classmethod
    def check_age(cls, v):
        if v is not None and v < 18:
            raise ValueError("Age must be at least 18")
        return v


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str
    admin_email: str
    items_per_page: int = Field(10, ge=1)


def create_settings(
    app_name: str, admin_email: str, items_per_page: int = 10
) -> Settings:
    return Settings(
        app_name=app_name, admin_email=admin_email, items_per_page=items_per_page
    )
