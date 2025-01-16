from typing import List

# T: O(N^2)
# S: O(N)
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

def minimum_mountain_removals(nums: List[int]) -> int:
    n = len(nums)

    # compute LIS up to each index
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # compute LDS from each index
    lds = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    # calculate the min removals
    max_mountain_len = 0
    for i in range(1, n - 1):  # i should be a peak so avoid the first and last element in the array
        if min(lis[i], lds[i]) > 1:  # a valid peak
            max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)

    return n - max_mountain_len