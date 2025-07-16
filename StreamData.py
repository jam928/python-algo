from sortedcontainers import SortedSet
from collections import defaultdict


class StreamData:
    def __init__(self, k):
        self.k = k
        self.freq = defaultdict(int)
        self.m = SortedSet(key=lambda x: (-x[0], x[1]))  # Sort by freq descending, then num ascending

    def addNum(self, num):
        cur_key = (self.freq[num], num)
        self.m.discard(cur_key)  # Remove old key

        self.freq[num] += 1
        new_key = (self.freq[num], num)

        if len(self.m) < self.k:
            self.m.add(new_key)
        else:
            last_elem = self.m[-1] if self.m else None
            if last_elem and last_elem[0] < new_key[0]:
                self.m.discard(last_elem)
                self.m.add(new_key)

    def getTopK(self):
        return [p[1] for p in self.m]


class Solution:
    def topKFrequent(self, nums, k):
        s = StreamData(k)
        ans = []
        for num in nums:
            s.addNum(num)
            ans.extend(s.getTopK())
        return ans
