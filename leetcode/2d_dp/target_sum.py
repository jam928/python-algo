from typing import List


# https://leetcode.com/problems/target-sum/

def find_target_sum_ways(nums: List[int], target: int) -> int:
    memo = {}

    def dfs(index, current_value):
        if current_value == target and index == len(nums):
            return 1

        if index >= len(nums):
            return 0

        if (index, current_value) in memo:
            return memo[(index, current_value)]

        negative_count = dfs(index + 1, current_value + (-1 * nums[index]))
        positive_count = dfs(index + 1, current_value + nums[index])
        ways = negative_count + positive_count

        memo[(index, current_value)] = ways
        return memo[(index, current_value)]

    return dfs(0, 0)

print(find_target_sum_ways(nums = [1,1,1,1,1], target = 3)) # 5
print(find_target_sum_ways(nums = [1], target = 1)) # 1
