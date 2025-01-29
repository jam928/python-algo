from typing import List

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# T: O(N)
# S: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_of_zeros = 0
        i = j = 0

        longest = 0
        while j < len(nums):
            if nums[j] == 0:
                num_of_zeros += 1

            while num_of_zeros > 1:
                if nums[i] == 0:
                    num_of_zeros -= 1
                i += 1

            longest = max(longest, j - i)

            j += 1

        return longest

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray(nums = [1,1,0,1])) # 3
    print(s.longestSubarray(nums = [0,1,1,1,0,1,1,0,1])) # 5
    print(s.longestSubarray(nums = [1,1,1])) # 2