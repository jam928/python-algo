from typing import List

# https://leetcode.com/problems/spiral-matrix-ii/

def generate_matrix(n: int) -> List[List[int]]:
    col_start = row_start = 0
    col_end = row_end = n - 1

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    count = 1

    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            matrix[row_start][i] = count
            count += 1

        row_start += 1

        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = count
            count += 1

        col_end -= 1

        # avoid duplicates
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                matrix[row_end][i] = count
                count += 1

        row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = count
                count += 1

        col_start += 1

    return matrix

print(generate_matrix(5))