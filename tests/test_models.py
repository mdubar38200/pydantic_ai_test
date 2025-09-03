from pydantic_ai_test import User


def test_user_model():
    u = User(id=1, email="a@example.com", name="Alice")
    assert u.email == "a@example.com"
