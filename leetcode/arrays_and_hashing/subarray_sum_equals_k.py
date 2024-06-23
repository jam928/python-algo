from typing import List

# https://leetcode.com/problems/subarray-sum-equals-k/description/

def subarray_sum(nums: List[int], k: int) -> int:
    count = current_sum = 0

    sum_map = {}

    sum_map[0] = 1

    for i in range(len(nums)):
        current_sum += nums[i]

        if (current_sum - k) in sum_map:
            count += sum_map[current_sum - k]

        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1

    return count

print(subarray_sum(nums = [1,1,1], k = 2)) # 2
print(subarray_sum(nums = [1,2,3], k = 3)) # 2
