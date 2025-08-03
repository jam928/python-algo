from typing import List

# https://leetcode.com/problems/sort-colors/description/
# T:O(N)
# S:O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
            all elements that are 0 will be < low
            all elements that are 1 will be between low and high
            all elements that are 2 will be > high
        """

        low = 0
        high = len(nums) - 1
        i = 0

        while i <= high:
            # if the element is zero then swap the element at low
            if nums[i] == 0:
                self.__swap(nums, i, low)
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                # swap i with high
                self.__swap(nums, i, high)
                high -= 1

    def __swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0,0,1,1,2,2]

    nums = [2,0,1]
    Solution().sortColors(nums)
    assert nums == [0,1,2]