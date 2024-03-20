from typing import List


# https://leetcode.com/problems/house-robber/
# T: O(n)
# S: O(n)

def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])

    for i in range(2, n):
        # the max at dp of i is 2 houses down plus the current element or its left neighbor
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[n - 1]


print(rob(nums=[1, 2, 3, 1]))  # 4
print(rob(nums=[2, 7, 9, 3, 1]))  # 12
