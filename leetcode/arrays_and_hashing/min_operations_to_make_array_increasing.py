# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/
from typing import List


def min_operations(nums: List[int]) -> int:
    count = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            count += nums[i - 1] + 1 - nums[i]
            nums[i] = nums[i - 1] + 1

    return count

print(min_operations([1,1,1])) # 3
print(min_operations([1,5,2,4,1])) # 14
print(min_operations([8])) # 0