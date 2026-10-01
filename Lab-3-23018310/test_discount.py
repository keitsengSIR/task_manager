"""Lab 3: equivalence-partition and boundary-value tests for calculate_discount.

Assumed specification (derived from the docstring, see Lab3Report.md):
  - price: int or float, valid domain price >= 0
  - is_premium: bool
  - premium users pay 80% of price (20% discount); others pay full price
  - invalid input must raise ValueError (bad value) or TypeError (bad type)
"""
import pytest
from app.tasks import calculate_discount


# --- Valid partitions ---------------------------------------------------
def test_tc01_premium_typical_price():
    assert calculate_discount(100, True) == pytest.approx(80)


def test_tc02_regular_typical_price():
    assert calculate_discount(100, False) == pytest.approx(100)


def test_tc03_premium_price_zero_lower_boundary():
    assert calculate_discount(0, True) == 0


def test_tc04_regular_price_zero_lower_boundary():
    assert calculate_discount(0, False) == 0


def test_tc05_premium_just_above_boundary():
    assert calculate_discount(0.01, True) == pytest.approx(0.008)


def test_tc06_premium_decimal_price():
    assert calculate_discount(19.99, True) == pytest.approx(15.992)


def test_tc07_premium_very_large_price():
    assert calculate_discount(1_000_000_000, True) == pytest.approx(800_000_000)


# --- Invalid price partitions -------------------------------------------
def test_tc08_negative_price_just_outside_boundary_premium():
    with pytest.raises(ValueError):
        calculate_discount(-0.01, True)


def test_tc09_negative_price_regular():
    with pytest.raises(ValueError):
        calculate_discount(-100, False)


def test_tc10_string_price_premium():
    with pytest.raises(TypeError):
        calculate_discount("100", True)


def test_tc11_string_price_regular():
    with pytest.raises(TypeError):
        calculate_discount("100", False)


def test_tc12_none_price_regular():
    with pytest.raises(TypeError):
        calculate_discount(None, False)


# --- Invalid is_premium partitions --------------------------------------
def test_tc13_is_premium_none():
    with pytest.raises(TypeError):
        calculate_discount(100, None)


def test_tc14_is_premium_string():
    with pytest.raises(TypeError):
        calculate_discount(100, "yes")


def test_tc15_is_premium_int_one():
    with pytest.raises(TypeError):
        calculate_discount(100, 1)