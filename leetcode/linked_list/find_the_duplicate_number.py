from typing import List


# https://leetcode.com/problems/find-the-duplicate-number/description/

# Tortoise and Hare Algorithm
def find_duplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast


print(find_duplicate([1, 3, 4, 2, 2]))  # 2
print(find_duplicate([3, 1, 3, 4, 2]))  # 3
