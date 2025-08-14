from typing import List


class Solution:
    # find the first decreasing element from the right
    # find the next larger element to swap
    # swap elements
    # reverse the suffix
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # if we found such an element
        if i >= 0:
            # find the next larger element to swap
            j = n - 1
            while nums[i] >= nums[j]:
                j -= 1
            # swap elements
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])

if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3]
    s.nextPermutation(arr)
    assert arr == [1, 3, 2]

    arr = [3,2,1]
    s.nextPermutation(arr)
    assert arr == [1, 2, 3]

    arr = [1,1,5]
    s.nextPermutation(arr)
    assert arr == [1,5,1]