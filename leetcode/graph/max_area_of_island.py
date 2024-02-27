from typing import List

# https://leetcode.com/problems/max-area-of-island/

# T: O(n * m)
# S: O(n * m)

def max_area_of_island(grid: List[List[int]]) -> int:
    def dfs(i, j, area):
        # check out of bounds
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return

        area[0] += 1
        grid[i][j] = -1
        # dfs left, right, up, & down
        dfs(i - 1, j, area)
        dfs(i + 1, j, area)
        dfs(i, j - 1, area)
        dfs(i, j + 1, area)

    max_area = [0]
    # iterate through each cell
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # update max area if area is higher than the current one
                area = [0]
                dfs(i, j, area)
                max_area[0] = max(max_area[0], area[0])

    return max_area[0]

print(max_area_of_island(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) # 6
print(max_area_of_island(grid = [[0,0,0,0,0,0,0,0]])) # 0