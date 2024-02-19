import heapq
from typing import List


# https://leetcode.com/problems/last-stone-weight/description/


def last_stone_weight(stones: List[int]) -> int:
    # store stones in pq
    pq = [-stone for stone in stones]
    heapq.heapify(pq)

    # retrieve two largest and follow conditions and put back in pq
    while len(pq) > 1:
        # get the two heaviest stones
        heavy_stone1 = -heapq.heappop(pq)
        heavy_stone2 = -heapq.heappop(pq)

        diff = heavy_stone1 - heavy_stone2
        if diff != 0:
            # place the new stone weight in queue
            heapq.heappush(pq, -diff)

    return -pq[0] if len(pq) == 1 else 0

print(last_stone_weight([2,7,4,1,8,1])) # 1
print(last_stone_weight([1])) # 1