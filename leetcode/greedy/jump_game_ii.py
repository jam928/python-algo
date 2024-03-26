from typing import List


# https://leetcode.com/problems/jump-game-ii/
# T: O(n)
# S: O(1)

def jump(nums: List[int]) -> int:
    result = 0
    l = r = 0

    while r < len(nums) - 1:
        biggest_jump = 0
        for i in range(l, r + 1):
            biggest_jump = max(biggest_jump, nums[i] + i)

        l = r + 1
        r = biggest_jump
        result += 1

    return result

print(jump([2,3,1,1,4])) # 2
print(jump([2,3,0,1,4])) # 2