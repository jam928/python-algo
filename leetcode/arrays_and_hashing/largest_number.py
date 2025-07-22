import functools
from typing import List
from functools import cmp_to_key
# https://leetcode.com/problems/largest-number/description/
# T: O(NLOGN)
# S: O(N + L) where L is the total number of digits in a given string

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            num1_str = str(num1)
            num2_str = str(num2)

            if (num1_str + num2_str) < (num2_str + num1_str):
                return 1

            if (num1_str + num2_str) > (num2_str + num1_str):
                return -1

            return 0

        # sort the integers based if a + b or b + a: whichever is greater
        nums_sorted = sorted(nums, key=cmp_to_key(compare))

        result = ''.join(map(str, nums_sorted))

        return result if result[0] != '0' else '0'

if __name__ == '__main__':
    assert Solution().largestNumber([10,2]) == "210"
    assert Solution().largestNumber([3,30,34,5,9]) == "9534330"