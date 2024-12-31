from collections import deque
from typing import List

# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

# T: O(n^2)
# S: O(n^2)
def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    result = 0

    row = len(grid)
    col = len(grid[0])

    if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
        return -1

    moves = [[-1, -1], [-1, 1], [1, -1], [1, 1], [1, 0], [-1, 0], [0, 1], [0, -1]]

    q = deque()

    q.append([0, 0])

    visited = [[False for _ in range(row)] for _ in range(col)]
    visited[0][0] = True

    while q:
        size = len(q)

        result += 1

        for i in range(size):
            current_position = q.popleft()

            if current_position[0] == row - 1 and current_position[1] == col - 1:
                return result

            for dx, dy in moves:
                next_i = current_position[0] + dx
                next_j = current_position[1] + dy

                if next_i < 0 or next_i >= row or next_j < 0 or next_j >= col or grid[next_i][next_j] == 1 or \
                        visited[next_i][next_j]:
                    continue

                visited[next_i][next_j] = True
                q.append((next_i, next_j))

    return -1

if __name__ == '__main__':
    print(shortest_path_binary_matrix([[0,1],[1,0]])) # 2
    print(shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]])) # 4
    print(shortest_path_binary_matrix([[1,0,0],[1,1,0],[1,1,0]])) # -1
