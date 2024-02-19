import heapq
from math import sqrt
from typing import List


# https://leetcode.com/problems/k-closest-points-to-origin/description/


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    # calculate the distances for each point to the origin and store in pq along with point
    pq = []

    for point in points:
        distance = sqrt(pow(point[0], 2) + pow(point[1], 2))
        heapq.heappush(pq, (distance, point))

    result = []
    # get the results up to k in the pq
    for i in range(0, k):
        distance, point = heapq.heappop(pq)
        result.append(point)
    return result

print(k_closest(points = [[1,3],[-2,2]], k = 1)) # [[-2,2]]
print(k_closest(points = [[3,3],[5,-1],[-2,4]], k = 2)) # [[3,3],[-2,4]]