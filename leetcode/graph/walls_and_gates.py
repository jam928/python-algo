from typing import List


def islands_and_treasure(grid: List[List[int]]) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                dfs(grid, i, j, 0)

    print(grid)

def dfs(grid, i, j, count):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == -1:
        return

    if count > grid[i][j]:
        return

    grid[i][j] = min(grid[i][j], count)
    dfs(grid, i + 1, j, count + 1)
    dfs(grid, i - 1, j, count + 1)
    dfs(grid, i, j + 1, count + 1)
    dfs(grid, i, j - 1, count + 1)

islands_and_treasure([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
])