import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = []
        self.k = k

        for num in nums:
            heapq.heappush(self.queue, num)

        # remove any elements if the queue is larger than K
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)

        # remove element from queue if its greater than k size
        if len(self.queue) > self.k:
            heapq.heappop(self.queue)

        return self.queue[0]

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # Output: 4
print(kthLargest.add(5))   # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))   # Output: 8
print(kthLargest.add(4))   # Output: 8