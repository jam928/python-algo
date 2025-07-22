from typing import List

# https://leetcode.com/problems/maximum-subarray/description/
# T: O(N)
# S: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = float('-inf')
        largest_sum = float('-inf')

        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            largest_sum = max(largest_sum, current_sum)

        return largest_sum

if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5,4,-1,7,8]) == 23