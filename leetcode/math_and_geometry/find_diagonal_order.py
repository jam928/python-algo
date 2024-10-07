from typing import List

# https://leetcode.com/problems/diagonal-traverse/

def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    if len(mat) == 1:
        return mat[0]

    row_start = 0
    row_end = len(mat)

    result = []
    reverse = True
    while row_start < row_end:
        i = row_start
        j = 0
        reverse = not reverse
        arr = []
        while i >= 0 and j < len(mat[0]):
            arr.append(mat[i][j])
            i -= 1
            j += 1
        if reverse:
            arr.reverse()
        result.extend(arr)
        row_start += 1

    col_start = 1
    col_end = len(mat[0]) - 1

    # reverse = False
    while col_start <= col_end:
        i = len(mat) - 1
        j = col_start
        reverse = not reverse
        arr = []
        while i >= 0 and j < len(mat[0]):
            arr.append(mat[i][j])
            i -= 1
            j += 1
        if reverse:
            arr.reverse()
        result.extend(arr)
        col_start += 1
    return result