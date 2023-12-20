from flatten_array import flatten_array


def test_flatten_nested_arrays():
    assert flatten_array([1, [2, 3], [4, 5, [6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_array([[1, 2], [3, [4, 5]], [6, [7]]]) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten_array([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]
