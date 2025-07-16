import heapq
from collections import defaultdict, Counter
from typing import List


# https://leetcode.com/problems/top-k-frequent-elements/
# T: O(N LOG N)
# S: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        freq_map = Counter(nums)

        pq = []

        for key, value in freq_map.items():
            heapq.heappush(pq, (-value, key))

        while len(result) < k and pq:
            result.append(heapq.heappop(pq)[1])

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
    print(s.topKFrequent([1], 1)) # [1]