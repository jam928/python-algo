from typing import List

# https://leetcode.com/problems/remove-element/description/

def remove_element(nums: List[int], val: int) -> int:
    if len(nums) == 0:
        return 0

    i = 0
    k = 0

    for j in range(len(nums)):
        if val == nums[j]:
            continue

        # swap the current number at i with the number at j
        nums[i] = nums[j]

        # increment the i pointer and k len
        i += 1
        k += 1

    return k

print(remove_element([3,2,2,3], 3)) # 2
print(remove_element([0,1,2,2,3,0,4,2], 2)) # 5