from src.task3 import check_number, first_n_primes, sum_1_to_100

def test_check_number_positive():
    assert check_number(5) == "positive"

def test_check_number_negative():
    assert check_number(-3) == "negative"

def test_check_number_zero():
    assert check_number(0) == "zero"

def test_check_number__negative_zero():
    assert check_number(-0) == "zero"

def test_first_10_primes():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert first_n_primes(10) == expected

def test_sum_1_to_100():
    assert sum_1_to_100() == 5050
