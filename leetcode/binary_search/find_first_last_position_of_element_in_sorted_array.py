# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# T: O(LOG N)
# S: O(1)

import bisect
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = bisect.bisect_left(nums, target)
        last_index = bisect.bisect_right(nums, target)

        first_position = first_index if 0 <= first_index < len(nums) and nums[first_index] == target else - 1
        last_position = last_index - 1 if last_index - 1 >= 0 and nums[last_index - 1] == target else - 1
        return [first_position, last_position]

if __name__ == '__main__':
    s = Solution()
    assert s.searchRange(nums = [5,7,7,8,8,10], target = 8) == [3,4]
    assert s.searchRange(nums = [5,7,7,8,8,10], target = 6) == [-1,-1]
    assert s.searchRange(nums=[], target=0) == [-1,-1]