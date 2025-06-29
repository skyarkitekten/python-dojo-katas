import pytest
from decimal import Decimal
from src.python_dojo_katas.pydantic_katas.basic_models import UserModel, ProductModel
from src.python_dojo_katas.pydantic_katas.validation_katas import (
    validate_user,
    validate_product,
)


def test_user_model():
    user = UserModel(username="testuser", email="test@example.com", age=25)
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.age == 25


def test_user_model_invalid_email():
    with pytest.raises(ValueError):
        UserModel(username="testuser", email="invalid-email", age=25)


def test_product_model():
    product = ProductModel(name="Test Product", price=Decimal("19.99"))
    assert product.name == "Test Product"
    assert product.price == Decimal("19.99")


def test_product_model_invalid_price():
    with pytest.raises(ValueError):
        ProductModel(name="Test Product", price=Decimal("-1"))


def test_validate_user():
    assert validate_user(username="validuser", email="valid@example.com") is True
    assert validate_user(username="", email="valid@example.com") is False


def test_validate_product():
    assert validate_product(name="Valid Product", price=10.0) is True
    assert validate_product(name="Valid Product", price=-5.0) is False
