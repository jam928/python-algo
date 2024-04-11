from typing import List


# T: O(MN)
# S: O(1)
# https://leetcode.com/problems/rotate-image/description/
def rotate(matrix: List[List[int]]) -> None:
    # rotate iteratively from top and bottom row
    start = 0
    end = len(matrix) - 1

    while start < end:
        for i in range(0, end - start):
            top = start
            bottom = end
            top_left = matrix[top][start + i]

            # replace top_left from bottom_left
            matrix[top][start + i] = matrix[bottom - i][start]

            # replace bottom_left from bottom_right
            matrix[bottom - i][start] = matrix[bottom][end - i]

            # replace bottom_right from top_right
            matrix[bottom][end - i] = matrix[top + i][end]

            # replace top_right from top_left
            matrix[top + i][end] = top_left

        start += 1
        end -= 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix2)
print(matrix2)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
