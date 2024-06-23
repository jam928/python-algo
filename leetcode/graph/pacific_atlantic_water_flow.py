from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    # keep track of the cells that are qualified as possible paths
    rows = len(heights)
    cols = len(heights[0])

    atlantic = [[False] * cols for _ in range(rows)]
    pacific = [[False] * cols for _ in range(rows)]

    # dfs on the first and last columns
    for i in range(0, rows):
        dfs(pacific, i, 0, 0, heights)
        dfs(atlantic, i, cols - 1, 0, heights)

    # dfs on the first and last rows
    for j in range(0, cols):
        dfs(pacific, 0, j, 0, heights)
        dfs(atlantic, rows - 1, j, 0, heights)

    result = []

    for i in range(0, rows):
        for j in range(0, cols):
            if atlantic[i][j] and pacific[i][j]:
                result.append(list([i, j]))

    return result


def dfs(ocean, i, j, height, heights):
    if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or height > heights[i][j] or ocean[i][j]:
        return

    ocean[i][j] = True
    height = heights[i][j]
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    for dx, dy in directions:
        dfs(ocean, dx+i, dy+j, height, heights)

print(pacific_atlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(pacific_atlantic(heights = [[1]])) # [[0,0]]