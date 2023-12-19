from typing import List


def array_sum(arr: List) -> float:
    def array_sum_helper(i, arr):
        if len(arr) - 1 == i:
            return arr[len(arr) - 1]

        return arr[i] + array_sum_helper(i + 1, arr)

    return 0 if len(arr) == 0 else array_sum_helper(0, arr)
