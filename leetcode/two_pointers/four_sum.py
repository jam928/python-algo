from typing import List

# T: O(N^3)
# S: O(K) # where k is the resulting number of quad arrays

# https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the array to compute quad sums seamlessly
        nums.sort()

        quadruplets = []
        n = len(nums)

        for i in range(0, n - 3):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # avoid duplicates
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                self.twoSum(nums, quadruplets, i, j, target)

        return quadruplets

    def twoSum(self, nums, quadruplets, i, j, target):
        # two ptr approach
        l = len(nums) - 1
        k = j + 1

        while k < l:
            quad_sum = nums[i] + nums[j] + nums[k] + nums[l]

            if quad_sum == target:
                # add the resulting quad sum to the quad array
                quadruplets.append([nums[i], nums[j], nums[k], nums[l]])

                k += 1
                l -= 1

                # removing any possible duplicates
                while k < l and nums[k] == nums[k - 1]:
                    k += 1  # skip same element to avoid duplicate quad sums
                while k < l and nums[l] == nums[l + 1]:
                    l -= 1  # skip same element to avoid duplicate quad sums
            elif quad_sum < target:
                k += 1
            else:
                l -= 1

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    print(s.fourSum(nums = [2,2,2,2,2], target = 8)) # [[2,2,2,2]]


