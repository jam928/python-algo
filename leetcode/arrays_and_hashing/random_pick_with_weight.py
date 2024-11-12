import random
from typing import List

# https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.pre_sum = [0] * n
        self.pre_sum[0] = w[0]

        for i in range(1, n):
            self.pre_sum[i] = self.pre_sum[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = random.randint(1, self.pre_sum[-1])  # get a random number b/t 1 and len of pre_sum
        result = self.binary_search(target)  # find the closest index with that target
        return result

    def binary_search(self, target):

        i = 0
        j = len(self.pre_sum) - 1

        while i <= j:

            mid = (i + j) // 2

            if self.pre_sum[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return j if i >= len(self.pre_sum) else i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()