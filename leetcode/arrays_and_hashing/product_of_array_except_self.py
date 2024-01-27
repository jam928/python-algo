# Calculate the products from left to right
# Then from right to left
# Then calcualte from both above
from typing import List


# https://leetcode.com/problems/product-of-array-except-self/

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    left_products = [1] * n
    right_products = [1] * n

    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product

    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product

    result = [left_products[i] * right_products[i] for i in range(n)]

    return result


print(product_except_self([1, 2, 3, 4]))  # [24,12,8,6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
