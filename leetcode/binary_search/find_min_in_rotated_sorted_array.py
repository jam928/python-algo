from typing import List


# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def find_min(nums: List[int]) -> int:
    start = 0
    n = len(nums)
    end = n - 1

    if start > end:
        return -1

    while start <= end:
        # find the mid using floor division
        mid = (start + end) // 2

        # min is found if the mid is greater than the next element
        if mid + 1 < n and (nums[mid] > nums[mid + 1]):
            return nums[mid + 1]

        # move the start pointer if the nums[start] is less than the nums[mid]
        if nums[start] <= nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return nums[0]


print(find_min(nums=[3, 4, 5, 1, 2]))  # 1
print(find_min(nums=[4, 5, 6, 7, 0, 1, 2]))  # 0
print(find_min(nums=[11, 13, 15, 17]))  # 11
print(find_min([4,5,1,2,3])) # 1