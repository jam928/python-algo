import heapq
from typing import List

# https://leetcode.com/problems/trapping-rain-water-ii
# T: O(M * N (LOG MN))
# S: O(M * N)
def trap_rain_water(height_map: List[List[int]]) -> int:
    # store the boundary heights in the min heap
    pq = []

    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if i == 0 or i == len(height_map) - 1 or j == 0 or j == len(height_map[0]) - 1:
                heapq.heappush(pq, (height_map[i][j], i, j))  # (height, i, j)

    result = 0
    max_h = 0
    while pq:
        # pop current min height
        current_h, i, j = heapq.heappop(pq)
        max_h = max(max_h, current_h)

        trapped_water = max_h - current_h
        result += trapped_water

        height_map[i][j] = -1  # mark current node as visited

        # add its neighbors
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dx, dy in moves:
            if 0 <= dx + i <= len(height_map) - 1 and 0 <= dy + j <= len(height_map[0]) - 1 and height_map[dx + i][
                dy + j] != -1:
                heapq.heappush(pq, (height_map[dx + i][dy + j], dx + i, dy + j))
                height_map[dx + i][dy + j] = -1

    return result


if __name__ == '__main__':
    height_map = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    print(trap_rain_water(height_map)) # 4

    height_map = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    print(trap_rain_water(height_map)) # 10

