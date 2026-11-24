import pytest
from pricing import calculate_price

def test_no_discount():
    assert calculate_price(100) == 100

def test_discount():
    assert calculate_price(100, 10) == 90

def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_price(100, 120)