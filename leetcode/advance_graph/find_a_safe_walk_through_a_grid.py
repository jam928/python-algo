from typing import List

# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
# T: O(M*N*H) where H is the height of current input
# S: O(M*N*H) where H is the height of current input

def find_safe_walk(grid: List[List[int]], health: int) -> bool:
    memo = {}

    def dfs(i, j, current_health):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 2 or current_health <= 0:
            return False

        if (i, j, current_health) in memo:
            return memo[(i, j, current_health)]

        if i == len(grid) - 1 and j == len(grid[0]) - 1 and current_health >= 1:
            return True

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        temp = grid[i][j]
        grid[i][j] = 2
        is_possible = []
        for dx, dy in moves:
            if 0 <= i + dx <= len(grid) - 1 and 0 <= j + dy <= len(grid[0]) - 1:
                is_possible.append(dfs(i + dx, j + dy, current_health - grid[i + dx][j + dy]))

        grid[i][j] = temp
        result = any(is_possible)
        memo[(i, j, current_health)] = result
        return result

    if grid[0][0] == 1:
        health -= 1

    return dfs(0, 0, health) if health >= 1 else False

if __name__ == '__main__':
    grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
    health = 1
    print(find_safe_walk(grid, health)) # True

    grid = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]]
    health = 3
    print(find_safe_walk(grid, health)) # False

    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    health = 5

    print(find_safe_walk(grid, health)) # True


