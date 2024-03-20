from typing import List


# https://leetcode.com/problems/house-robber-ii/
# T: O(n)
# S: O(n)

def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    elif n == 3:
        return max(nums[0], nums[1], nums[2])

    # keep track from 0 to n-2 to not include last element
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    max_amount = 0
    for i in range(2, n - 1):
        # the max at dp of i is 2 houses down plus the current element or its left neighbor
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        max_amount = max(max_amount, dp[i])

    # not include the first element
    dp1 = [0 for _ in range(n)]
    dp1[0] = 0
    dp1[1] = nums[1]

    for i in range(2, n):
        # the max at dp of i is 2 houses down plus the current element or its left neighbor
        dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        max_amount = max(max_amount, dp1[i])

    return max_amount


print(rob(nums=[2, 3, 2]))  # 3
print(rob(nums=[1, 2, 3, 1]))  # 4
print(rob(nums=[1, 2, 3]))  # 3
