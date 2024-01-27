from typing import List


# https://leetcode.com/problems/pascals-triangle/

def generate(num_rows: int) -> List[List[int]]:
    triangle = [[1]]

    for i in range(1, num_rows):
        prev_row = triangle[i - 1]

        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle
