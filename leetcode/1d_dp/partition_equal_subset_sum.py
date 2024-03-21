from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum/
# T: O(2^n)
# S: O(n^2)

def can_partition(nums: List[int]) -> bool:
    sum_of_nums = sum(nums)

    if sum_of_nums % 2 != 0:
        return False

    sum_of_nums /= 2

    memo = {}

    def dfs(current_sum, index):
        if current_sum == 0:
            return True

        if index >= len(nums) or current_sum < 0:
            return False

        if (current_sum, index) in memo:
            return memo[(current_sum, index)]

        # dfs with adding the current element or skipping it
        result = dfs(current_sum - nums[index], index + 1) or dfs(current_sum, index + 1)
        memo[(current_sum, index)] = result
        return result

    return dfs(sum_of_nums, 0)


print(can_partition(nums=[1, 5, 11, 5]))  # True
print(can_partition(nums=[1, 2, 3, 5]))  # False
