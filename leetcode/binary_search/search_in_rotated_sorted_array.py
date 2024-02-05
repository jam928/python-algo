from typing import List


# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums: List[int], target: int) -> int:
    start = 0
    n = len(nums)
    end = n - 1

    if start > end:
        return -1

    while start <= end:
        # find the mid using floor division
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid  # return the index

        # start to mid is sorted
        if nums[start] <= nums[mid]:
            # if the target is between is start and mid move the end pointer closer to mid - 1
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # if the target is between is mid and end move the start pointer closer to the right by mid + 1
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
print(search(nums=[1], target=0))  # -1
