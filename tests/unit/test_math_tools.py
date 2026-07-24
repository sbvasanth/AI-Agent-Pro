from src.tools.math_tools import add, subtract, multiply, divide
import pytest

# -------------------------
# ADD
# -------------------------


def test_add_positive_numbers():
    assert add.invoke({"a": 5, "b": 10}) == 15


def test_add_negative_numbers():
    assert add.invoke({"a": -5, "b": -10}) == -15


def test_add_zero():
    assert add.invoke({"a": 0, "b": 100}) == 100


# -------------------------
# SUBTRACT
# -------------------------


def test_subtract_positive():
    assert subtract.invoke({"a": 20, "b": 5}) == 15


def test_subtract_negative():
    assert subtract.invoke({"a": -5, "b": -5}) == 0


# -------------------------
# MULTIPLY
# -------------------------


def test_multiply_positive():
    assert multiply.invoke({"a": 6, "b": 7}) == 42


def test_multiply_zero():
    assert multiply.invoke({"a": 999, "b": 0}) == 0


def test_multiply_negative():
    assert multiply.invoke({"a": -5, "b": 4}) == -20


# -------------------------
# DIVIDE
# -------------------------


def test_divide():
    assert divide.invoke({"a": 10, "b": 2}) == 5


def test_divide_float():
    assert divide.invoke({"a": 7, "b": 2}) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide.invoke({"a": 10, "b": 0})
