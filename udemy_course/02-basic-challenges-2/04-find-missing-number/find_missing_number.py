def find_missing_number(arr):
    if len(arr) == 0:
        return 1

    n = len(arr) + 1

    expected_sum = n * (n+1) / 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum
