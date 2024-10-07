from typing import List

# https://leetcode.com/problems/toeplitz-matrix/

def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    if len(matrix) == 1:
        return True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            initial_element = matrix[i][j]
            if initial_element == 100:
                continue
            x = i
            y = j
            while x < len(matrix) and y < len(matrix[0]):
                if initial_element != matrix[x][y]:
                    return False
                matrix[x][y] = 100  # use 100 to avoid iterating the diagonal again
                x += 1
                y += 1

    return True

print(is_toeplitz_matrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]])) # True
print(is_toeplitz_matrix(matrix = [[1,2],[2,2]])) # False