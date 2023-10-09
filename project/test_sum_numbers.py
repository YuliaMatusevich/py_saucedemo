from math_functions import sum_num

def test_add_numbers_positive():
    assert sum_num(2, 8) == 10


def test_add_numbers_negative():
    assert sum_num(5, 8) == 12
