
from typing import List

# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
# T: O(NLOGN)
# S: O(1)

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        result = 0
        total = 0

        for j in range(len(nums)):
            total += nums[j]

            while nums[j] * (j - i + 1) > total + k:
                total -= nums[i]
                i += 1

            result = max(result, (j - i + 1))

        return result

if __name__ == '__main__':
    s = Solution()

    assert s.maxFrequency([1,2,4], 5) == 3
    assert s.maxFrequency([1,4,8,13], 5) == 2
    assert s.maxFrequency([3,9,6], 2) == 1