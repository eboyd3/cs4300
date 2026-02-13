import pytest
from src.task2 import add_integers, multiply_floats, greet, is_even

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 7),
        (0, 5, 5),
        (-2, 3, 1),
        (-3, -4, -7),
    ]
)
def test_add_integers(a, b, expected):
    assert add_integers(a, b) == expected

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2.5, 4.0, 10.0),
        (0.0, 5.0, 0.0),
        (-2.0, 3.0, -6.0),
        (1.5, 2.0, 3.0),
    ]
)
def test_multiply_floats(x, y, expected):
    assert multiply_floats(x, y) == expected

@pytest.mark.parametrize(
    "name, expected",
    [
        ("Fred", "Hello, Fred!"),
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
    ]
)
def test_greet(name, expected):
    assert greet(name) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (4, True),
        (5, False),
        (0, True),
        (-2, True),
        (-3, False),
    ]
)
def test_is_even(number, expected):
    assert is_even(number) is expected
