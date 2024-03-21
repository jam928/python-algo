from typing import List

# https://leetcode.com/problems/longest-increasing-subsequence/

# T: O(n^2)
# S: O(n)

def length_of_LIS(nums: List[int]) -> int:
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(length_of_LIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(length_of_LIS(nums=[0, 1, 0, 3, 2, 3]))  # 4
print(length_of_LIS(nums=[7, 7, 7, 7, 7, 7, 7]))  # 1
