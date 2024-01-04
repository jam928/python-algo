from max_subarray_quadratic import max_subarray_quadratic


def test_maximum_subarray_using_squared_solution():
    arr1 = [2, 5, 3, 1, 11, 7, 6, 4]
    k1 = 3
    max_subarray_quadratic(arr1, k1) == 24

    arr2 = [-2, -5, -3, -1, -11, -7, -6, -4]
    k2 = 4
    max_subarray_quadratic(arr2, k2) == -9
