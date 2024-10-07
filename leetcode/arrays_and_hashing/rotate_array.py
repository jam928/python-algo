from typing import List

# https://leetcode.com/problems/rotate-array/

def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    temp = [0 for _ in range(n)]

    for i in range(n):
        m = (i + k) % n
        temp[m] = nums[i]

    for i in range(n):
        nums[i] = temp[i]

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k) # [5,6,7,1,2,3,4]
print(nums)

nums = [-1,-100,3,99]
k = 2
rotate(nums, k) # [3,99,-1,-100]
print(nums)