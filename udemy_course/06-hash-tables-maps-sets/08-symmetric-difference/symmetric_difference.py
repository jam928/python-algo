from typing import List


def symmetric_difference(arr1: List[int], arr2: List[int]) -> List[int]:
    # Store the elements of arr1 and arr2 in set
    arr1_set = set(arr1)
    arr2_set = set(arr2)

    # Iterate thru elements of list1 and list2 and if the element is not in set then add to result array
    result = []

    for e in arr1:
        if e not in arr2_set:
            result.append(e)

    for e in arr2:
        if e not in arr1_set:
            result.append(e)

    return result
