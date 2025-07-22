from typing import List

# https://leetcode.com/problems/jump-game/description/
# T: O(N)
# S: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = nums[0]

        n = len(nums) - 1

        while i <= j:
            if j >= n:
                return True

            j = max(j, nums[i] + i)
            i += 1

        return False

if __name__ == '__main__':
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False