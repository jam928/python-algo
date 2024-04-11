from typing import List


# T: O(MN)
# S: O(1)
# https://leetcode.com/problems/spiral-matrix/description/

def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []

    row_start = 0
    row_end = len(matrix) - 1

    col_start = 0
    col_end = len(matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        # add the left to right top elements
        for i in range(col_start, col_end + 1):
            result.append(matrix[row_start][i])

        row_start += 1  # increment the row_start for the next iteration

        # iterate from topright to bottom right
        for i in range(row_start, row_end + 1):
            result.append(matrix[i][col_end])

        col_end -= 1  # decrement the col_end ptr for the next iteration

        # iterate from bottom right to bottom left
        # verify we have not overlap row ptr to avoid duplicates
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                result.append(matrix[row_end][i])

        row_end -= 1  # decrement the row_end ptr for the next iteration

        # iterate from bottom right to top left
        # verify we have not overlap col ptr to avoid duplicates
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                result.append(matrix[i][col_start])

        col_start += 1  # increment the col_start ptr for the next iteration

    return result


print(spiral_order(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
print(spiral_order(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
