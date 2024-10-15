import functools
from typing import List

# https://leetcode.com/problems/largest-number/description/

class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        # sort the integers based if a + b or b + a: whichever is greater
        nums_sorted = sorted(nums, key=functools.cmp_to_key(self.compare))

        result = ''.join(map(str, nums_sorted))

        return result if result[0] != '0' else '0'

    def compare(self, x, y):
        str1 = str(x)
        str2 = str(y)

        if (str1 + str2) < (str2 + str1):
            return 1

        if (str1 + str2) > (str2 + str1):
            return -1

        return 0

if __name__ == '__main__':
    print(Solution().largestNumber([10,2])) # 210
    print(Solution().largestNumber([3,30,34,5,9])) # 9534330