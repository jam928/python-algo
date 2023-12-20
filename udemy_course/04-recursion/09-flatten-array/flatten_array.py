from typing import List


def flatten_array(arr: List[int]) -> List[int]:
    def flatten_array_helper(i, arr, result):
        if len(arr) == i:
            return

        if isinstance(arr[i], list):
            flatten_array_helper(0, arr[i], result)
        else:
            result.append(arr[i])
        flatten_array_helper(i + 1, arr, result)

    result = []
    flatten_array_helper(0, arr, result)
    return result
