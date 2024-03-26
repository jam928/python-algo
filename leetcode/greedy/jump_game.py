from typing import List

# https://leetcode.com/problems/jump-game/description/
# T: O(N)
# S: O(1)

def can_jump(nums: List[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False


print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
