from typing import List

# https://leetcode.com/problems/rotate-array/
# T: O(N)
# S: O(N)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = [0 for _ in range(n)]

        for i in range(n):
            m = (i + k) % n
            temp[m] = nums[i]

        for i in range(n):
            nums[i] = temp[i]

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

    nums = [-1,-100,3,99]
    k = 2
    s.rotate(nums, k)
    assert nums == [3,99,-1,-100]