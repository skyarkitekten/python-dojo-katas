from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class UserModel(BaseModel):
    username: str
    email: EmailStr
    age: int

    @field_validator("age")
    def validate_age(cls, age: int) -> int:
        if age < 0:
            raise ValueError("Age must be a positive integer.")
        return age


class ProductModel(BaseModel):
    name: str
    price: Decimal = Field(gt=0, decimal_places=2)  # price must be greater than 0
    description: Optional[str] = None

    @field_validator("price")
    @classmethod
    def validate_price(cls, price: Decimal) -> Decimal:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        return price
