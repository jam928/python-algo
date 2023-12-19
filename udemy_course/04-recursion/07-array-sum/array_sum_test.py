from array_sum import array_sum


def test_calculate_sum_of_array_using_recursion():
    assert array_sum([1, 2, 3, 4, 5]) == 15
    assert array_sum([-1, -2, -3, -4, -5]) == -15
    assert array_sum([]) == 0
    assert array_sum([1,2]) == 3
    assert array_sum([1]) == 1