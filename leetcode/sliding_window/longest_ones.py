from collections import deque
from typing import List

# https://leetcode.com/problems/max-consecutive-ones-iii/
# T: O(n)
# S: O(1)

def longest_ones(nums: List[int], k: int) -> int:
    max_w = 0
    num_zeros = 0
    n = len(nums)

    l = 0

    for r in range(n):
        if nums[r] == 0:
            num_zeros += 1

        while num_zeros > k:  # shrink window
            if nums[l] == 0:
                num_zeros -= 1
            l += 1

        w = r - l + 1
        max_w = max(max_w, w)

    return max_w

if __name__ == '__main__':
    print(longest_ones(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)) # 6
    print(longest_ones(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)) # 10