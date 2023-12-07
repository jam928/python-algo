import sum_of_even_squares as s


def test_sum_of_even_squares():
    assert s.sum_of_even_squares([1, 2, 3, 4, 5]) == 20
    assert s.sum_of_even_squares([-1, 0, 1, 2, 3, 4]) == 20
    assert s.sum_of_even_squares([]) == 0
