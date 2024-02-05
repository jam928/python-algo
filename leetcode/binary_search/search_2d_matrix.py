# Use binary search twice
# Binary search to find the correct row
# Binary Search to find the correct element of the row
from typing import List


# https://leetcode.com/problems/search-a-2d-matrix/description/
# T: O(log(m) + log(n))
# S: O(1)

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    top_row = 0
    bottom_row = len(matrix) - 1

    row_num = -1

    while top_row <= bottom_row:
        mid = (top_row + bottom_row) // 2
        mid_row = matrix[mid]

        left = mid_row[0]
        right = mid_row[len(mid_row) - 1]

        # if the number is between the left & right set the row_num and break out of the loop
        if left <= target <= right:
            row_num = mid
            break
        if left < target:  # increasing the left if its too low
            top_row = mid + 1
        else:
            bottom_row = mid - 1

    if row_num == -1:  # no row num found
        return False

    arr = matrix[row_num]

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))  # true
print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))  # false
