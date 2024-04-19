import heapq
from collections import defaultdict
from typing import List


# Time complexity: O(E + N * log N)
# Space complexity: O(E + N)
# https://leetcode.com/problems/network-delay-time/description/

def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    adj_list = defaultdict(list)

    # add the u with its neighbors(v) and its weight to the adjlist
    for u, v, w in times:
        adj_list[u].append((v, w))

    # use pq and bfs for djstrka
    pq = [(0, k)]
    visited = set()

    heapq.heappush(pq, (0, k))

    max_time = 0

    while len(pq) != 0:
        pair = heapq.heappop(pq)
        node = pair[1]
        weight = pair[0]

        if node in visited:
            continue

        visited.add(node)
        max_time = max(max_time, weight)
        neighbors = adj_list[node]

        for neighbor in neighbors:
            if neighbor[0] in visited:
                continue
            heapq.heappush(pq, (neighbor[1] + weight, neighbor[0]))

    return max_time if len(visited) == n else -1


print(network_delay_time(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))  # 2
print(network_delay_time(times=[[1, 2, 1]], n=2, k=1))  # 1
print(network_delay_time(times=[[1, 2, 1]], n=2, k=2))  # -1
