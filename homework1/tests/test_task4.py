from src.task4 import calculate_discount

def test_with_integers():
    assert calculate_discount(100, 20) == 80

def test_with_floats():
    assert calculate_discount(99.99, 10.0) == 89.991

def test_int_float():
    assert calculate_discount(200, 12.5) == 175.0


def test_discount_float_int():
    assert calculate_discount(150.0, 10) == 135.0

def test_zero_discount():
    assert calculate_discount(50, 0) == 50
