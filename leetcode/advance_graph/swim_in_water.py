import heapq

# https://leetcode.com/problems/swim-in-rising-water/description/

# T: O(N^2 log N) since its NxN matrix and logn operations for using the heap
# S: (N ^ 2) for storing the visited values in the boolean matrix

def swim_in_water(grid):
    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Priority queue to store [maxValueSoFar, i, j]
    pq = [(grid[0][0], 0, 0)]  # (elevation, i, j)
    visited[0][0] = True

    # Directions: RIGHT, DOWN, UP, LEFT
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        current_path_max_value, i, j = heapq.heappop(pq)

        # Check if we reached the destination
        if i == n - 1 and j == n - 1:
            return current_path_max_value

        # Explore adjacent cells
        for dx, dy in directions:

            # Check bounds and if cell is unvisited
            if 0 <= dx + i < n and 0 <= dy + j < n and not visited[dx + i][dy + j]:
                visited[dx + i][dy + j] = True
                heapq.heappush(pq, (max(current_path_max_value, grid[dx + i][dy + j]), dx + i, dy + j))

    return 0

if __name__ == '__main__':
    grid = [[0, 2], [1, 3]]
    print(swim_in_water(grid)) # 3

    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(swim_in_water(grid)) # 16

