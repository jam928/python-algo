from typing import List


def length_of_LIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1 for _ in range(n)]
    max_length = 1

    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                dp[j] = max(dp[j], dp[i] + 1)
                max_length = max(max_length, dp[j])

    return max_length


print(length_of_LIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(length_of_LIS(nums=[0, 1, 0, 3, 2, 3]))  # 4
print(length_of_LIS(nums=[7, 7, 7, 7, 7, 7, 7]))  # 1
