from number_range import number_range


def test_calculating_the_range_of_numbers():
    assert number_range(1, 5) == [1, 2, 3, 4, 5]
    assert number_range(3, 10) == [3, 4, 5, 6, 7, 8, 9, 10]
    assert number_range(7, 7) == [7]
