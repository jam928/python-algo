from typing import List


# https://leetcode.com/problems/non-decreasing-array/

def check_possibility(nums: List[int]) -> bool:
    changed = False
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        if changed:
            return False
        # we want to decrease left element
        # [3, 4, 2]
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]

        changed = True

    return True

print(check_possibility([4,2,3])) # True
print(check_possibility([4,2,3,1])) # False
print(check_possibility([4,2,1])) # False