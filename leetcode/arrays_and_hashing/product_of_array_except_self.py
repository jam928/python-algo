# Calculate the products from left to right
# Then from right to left
# Then calcualte from both above
from typing import List


# https://leetcode.com/problems/product-of-array-except-self/

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    product = 1
    for i in range(n):
        result[i] *= product
        product *= nums[i]

    product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= product
        product *= nums[i]

    return result


print(product_except_self([1, 2, 3, 4]))  # [24,12,8,6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
