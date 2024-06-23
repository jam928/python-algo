from typing import List

# T: O(n)
# S: O(1)
# https://leetcode.com/problems/maximum-product-subarray/description/

def max_product(nums: List[int]) -> int:
    current_min = 1
    current_max = 1

    result = 0

    for num in nums:
        temp = current_max
        current_max = max(current_max * num, current_min * num, num)
        current_min = min(current_min * num, temp * num, num)
        result = max(result, current_max)

    return result

print(max_product(nums = [2,3,-2,4])) # 6
print(max_product(nums = [-2,0,-1])) # 2
