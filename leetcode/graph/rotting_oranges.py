from collections import deque
from typing import List

# T: O(m * n)
# S: O(m * n)

# https://leetcode.com/problems/rotting-oranges/description/

def oranges_rotting(grid: List[List[int]]) -> int:
    q = deque()
    fresh = 0
    minutes = 0

    # count the amount of fresh ones and put the rotten in the queue
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                fresh += 1
            if grid[i][j] == 2:
                q.append((i, j))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # check its neighbor if fresh and rot them if so
    # and add to queue to repeat process for the new rotten ones
    while fresh > 0 and q:
        length = len(q)
        for _ in range(length):
            (x, y) = q.popleft()

            for dx, dy in directions:
                i = x + dx
                j = y + dy

                # if in bounds and nonrotten, make rotten
                # and add to queue for next iteration
                if (i in range(len(grid)) and j in range(len(grid[0])) and grid[i][j] == 1):
                    grid[i][j] = 2
                    q.append((i, j))
                    fresh -= 1

        minutes += 1

    return minutes if fresh == 0 else -1

print(oranges_rotting(grid = [[2,1,1],[1,1,0],[0,1,1]])) # 4
print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
print(oranges_rotting(grid = [[0,2]])) # 0