import bisect
import random
from typing import List

# https://leetcode.com/problems/random-pick-with-weight/
# T: O(logN)
# S: O(N)

class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.pre_sum = [0] * n
        self.pre_sum[0] = w[0]

        for i in range(1, n):
            self.pre_sum[i] = self.pre_sum[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = random.randint(1, self.pre_sum[-1])  # get a random number b/t 1 and len of pre_sum
        result = bisect.bisect_left(self.pre_sum, target)  # find the closest index with that target
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()