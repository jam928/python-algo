from typing import List

# https://leetcode.com/problems/find-peak-element/description/

def find_peak_element(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        # left neighbor greater than at m
        # then search left side of mid - 1
        if mid > 0 and nums[mid] < nums[mid - 1]:
            r = mid - 1
        # right neighbor greater than at m
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            return mid

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(find_peak_element(nums)) # 2

    nums2 = [1,2,1,3,5,6,4]
    print(find_peak_element(nums2)) # 5
