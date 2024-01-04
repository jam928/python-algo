from max_subarray_linear import max_subarray_sum


def test_maximum_subarray_using_linear_solution():
    arr1 = [2, 5, 3, 1, 11, 7, 6, 4]
    k1 = 3
    max_subarray_sum(arr1, k1) == 24

    arr2 = [-2, -5, -3, -1, -11, -7, -6, -4]
    k2 = 4
    max_subarray_sum(arr2, k2) == -9
