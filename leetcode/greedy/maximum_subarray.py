from typing import List

# https://leetcode.com/problems/maximum-subarray/description/
# T: O(N)
# S: O(1)

def max_sub_array(nums: List[int]) -> int:
    current_sum = 0
    max_sum = float('-inf')

    for num in nums:
        # update current sum by the current number or current number plus the current sum
        current_sum = max(num, num + current_sum)
        # update max sum
        max_sum = max(max_sum, current_sum)

    return nums[0] if len(nums) == 1 else max_sum

print(max_sub_array(nums = [-2,1,-3,4,-1,2,1,-5,4])) # 6
print(max_sub_array([1])) # 1
print(max_sub_array([5,4,-1,7,8])) # 23