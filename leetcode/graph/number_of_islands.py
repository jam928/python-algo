from typing import List


# https://leetcode.com/problems/number-of-islands/

# T: O(n * m)
# S: O(n * m)

def num_islands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        # check out of bounds
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        # dfs left, right, up, & down
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    num_of_islands = 0
    # iterate through each cell
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                dfs(i, j)
                num_of_islands += 1

    return num_of_islands

print(num_islands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1

print(num_islands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3