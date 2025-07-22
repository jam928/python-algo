# Calculate the products from left to right
# Then from right to left
# Then calcualte from both above
from typing import List


# https://leetcode.com/problems/product-of-array-except-self/
# T: O(N)
# S: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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

if __name__ == '__main__':
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24,12,8,6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0,0,9,0,0]
