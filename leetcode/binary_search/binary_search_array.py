from typing import List

# https://leetcode.com/problems/binary-search/

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        # get the mid point
        mid = (left + right) // 2

        # if the nums at mid equals target then return mid
        if nums[mid] == target:
            return mid
        # if the number at mid is less than target start, move the left ptr to mid + 1
        elif nums[mid] < target:
            left = mid + 1
        # move the right ptr mid - 1 to get lower numbers
        else:
            right = mid - 1

    return -1

print(search([-1,0,3,5,9,12], 9)) # 4
print(search([-1,0,3,5,9,12], 2)) # -1