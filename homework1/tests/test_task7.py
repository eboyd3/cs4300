from src.task7 import calculate_mean

def test_calculate_mean_integers():
    numbers = [1, 2, 3, 4, 5]
    assert calculate_mean(numbers) == 3.0

def test_calculate_mean_floats():
    numbers = [1.5, 2.5, 3.5]
    assert calculate_mean(numbers) == 2.5

def test_calculate_mean_mixed():
    numbers = [1, 2.5, 3, 4.5]
    assert calculate_mean(numbers) == 2.75
