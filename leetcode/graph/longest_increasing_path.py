from typing import List

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

# T: O(MN)
# S: O(MN)
def longest_increasing_path(matrix: List[List[int]]) -> int:
    dp = {}  # (i, j) -> LIP

    def dfs(i, j, prev_val):
        if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev_val):
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        res = 1
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dx, dy in moves:
            res = max(res, 1 + dfs(i + dx, j + dy, matrix[i][j]))

        dp[(i, j)] = res
        return res

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(i, j, -1)
    return max(dp.values())

if __name__ == '__main__':
    print(longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]])) # 4
    print(longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]])) # 4
    print(longest_increasing_path(matrix = [[1]])) # 1