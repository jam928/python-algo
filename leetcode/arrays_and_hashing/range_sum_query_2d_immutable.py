from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # pad the dp with extra 0's in the left and top
        self.dp = [[0] * (COLS+1) for _ in range(ROWS+1)]

        # calculate prefix sum for rows and cols in the matrix
        for r in range(len(self.dp) - 1):
            for c in range(len(self.dp[0]) - 1):
                self.dp[r+1][c+1] = matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_a = self.dp[row2+1][col2+1]
        region_b = self.dp[row1][col2+1]
        region_c = self.dp[row2+1][col1]
        region_d = self.dp[row1][col1]

        return region_a - region_b - region_c + region_d




if __name__ == '__main__':
    num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(num_matrix.sum_region(2, 1, 4, 3)) # return 8
    print(num_matrix.sum_region(1, 1, 2,2))  # return 11
    print(num_matrix.sum_region(1, 2, 2, 4)) # return 12
