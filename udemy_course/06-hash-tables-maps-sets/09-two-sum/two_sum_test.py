from two_sum import two_sum


def test_two_sum_1():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    assert set(result) == {0, 1}


def test_two_sum_2():
    nums = [3, 2, 4]
    target = 6
    result = two_sum(nums, target)
    assert set(result) == {1, 2}


def test_two_sum_3():
    nums = [3, 3]
    target = 6
    result = two_sum(nums, target)
    assert set(result) == {0, 1}
