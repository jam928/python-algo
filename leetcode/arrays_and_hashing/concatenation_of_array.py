# https://leetcode.com/problems/concatenation-of-array/description/
from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    return nums + nums


print(get_concatenation([1, 2, 1]))
print(get_concatenation([1, 3, 2, 1]))
