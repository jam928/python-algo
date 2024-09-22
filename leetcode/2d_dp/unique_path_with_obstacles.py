from typing import List

#https://leetcode.com/problems/unique-paths-ii/description/

def unique_path_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    m = len(obstacle_grid)
    n = len(obstacle_grid[0])

    memo = {}

    def helper(i, j):
        if i >= m or j >= n or obstacle_grid[i][j] == 1:
            return 0

        if i == m - 1 and j == n - 1:
            return 1

        if (i, j) in memo:
            return memo[(i, j)]

        memo[(i, j)] = helper(i + 1, j) + helper(i, j + 1)
        return memo[(i, j)]

    return helper(0, 0)

obstacle_grid = [[0,0,0],[0,1,0],[0,0,0]]
print(unique_path_with_obstacles(obstacle_grid)) # 2

obstacle_grid = [[0,1],[0,0]]
print(unique_path_with_obstacles(obstacle_grid)) # 1