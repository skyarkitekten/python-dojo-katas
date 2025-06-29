"""Validation kata exercises for practicing Pydantic validation patterns."""

from typing import Any, Dict, List, Union, Optional
from pydantic import ValidationError
from decimal import Decimal
from .basic_models import UserModel, ProductModel


def validate_user(username: str, email: str, age: int = 25) -> bool:
    """
    Validate user data and return True if valid, False otherwise.

    Args:
        username: Username string
        email: Email address
        age: User age (default: 25)

    Returns:
        bool: True if validation passes, False otherwise
    """
    # Check for empty username before attempting to create the model
    if not username or username.strip() == "":
        return False

    try:
        UserModel(username=username, email=email, age=age)
        return True
    except ValidationError:
        return False


def validate_product(
    name: str, price: float, description: Optional[str] = None
) -> bool:
    """
    Validate product data and return True if valid, False otherwise.

    Args:
        name: Product name
        price: Product price
        description: Optional product description

    Returns:
        bool: True if validation passes, False otherwise
    """
    try:
        ProductModel(name=name, price=Decimal(str(price)), description=description)
        return True
    except ValidationError:
        return False


def validate_user_dict(user_data: Dict[str, Any]) -> Union[UserModel, List[Any]]:
    """
    Validate user data from dictionary and return model or errors.

    Args:
        user_data: Dictionary containing user data

    Returns:
        Union[UserModel, List[Any]]: Valid model or list of validation errors
    """
    try:
        user = UserModel(**user_data)
        return user
    except ValidationError as e:
        return e.errors()


def validate_product_dict(
    product_data: Dict[str, Any],
) -> Union[ProductModel, List[Any]]:
    """
    Validate product data from dictionary and return model or errors.

    Args:
        product_data: Dictionary containing product data

    Returns:
        Union[ProductModel, List[Any]]: Valid model or list of validation errors
    """
    try:
        product = ProductModel(**product_data)
        return product
    except ValidationError as e:
        return e.errors()


# Kata Exercise: Custom validation functions
def is_valid_username(username: str) -> bool:
    """Check if username is valid (alphanumeric, 3-20 chars)."""
    return username.isalnum() and 3 <= len(username) <= 20


def is_valid_age(age: int) -> bool:
    """Check if age is valid (0-120)."""
    return 0 <= age <= 120


def validate_user_custom(username: str, email: str, age: int) -> Dict[str, Any]:
    """
    Custom validation with detailed error reporting.

    Returns:
        Dict with 'valid' boolean and 'errors' list
    """
    errors = []

    if not is_valid_username(username):
        errors.append("Username must be alphanumeric and 3-20 characters")

    if not is_valid_age(age):
        errors.append("Age must be between 0 and 120")

    # Use Pydantic for email validation
    try:
        UserModel(username=username, email=email, age=age)
    except ValidationError as e:
        for error in e.errors():
            if error["loc"][0] == "email":
                errors.append("Invalid email format")

    return {"valid": len(errors) == 0, "errors": errors}
