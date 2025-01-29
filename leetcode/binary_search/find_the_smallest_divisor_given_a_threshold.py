from math import ceil
from typing import List

# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# T: O(N LOG S)
# S: O(1)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            average_sum = 0
            # calculate average
            for num in nums:
                average_sum += ceil(num / mid)

            if average_sum > threshold:
                left = mid + 1
            else:
                right = mid

        return left

if __name__ == '__main__':
    s = Solution()
    print(s.smallestDivisor(nums = [1,2,5,9], threshold = 6)) # 5
    print(s.smallestDivisor(nums = [44,22,33,11,1], threshold = 5)) # 44