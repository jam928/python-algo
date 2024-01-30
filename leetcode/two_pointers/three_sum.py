from typing import List


# https://leetcode.com/problems/3sum/

def three_sum(nums: List[int]) -> List[List[int]]:
    triplets = []

    # sort the numbers in increasing order for the triplets to be in order
    nums.sort()

    n = len(nums)

    # iterate from 0 to n-2
    for i in range(n - 2):
        # avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        two_sum(nums, triplets, i)

    return triplets


def two_sum(nums, triplets, i):
    # use two pointer approach
    j = i + 1
    k = len(nums) - 1

    while j < k:
        sum_of_triple = nums[i] + nums[j] + nums[k]
        if sum_of_triple == 0:
            triplets.append([nums[i], nums[j], nums[k]])

            j += 1
            k -= 1

            # avoid duplicates to get unique triplets
            while j < k and nums[j] == nums[j - 1]:
                j += 1

            while j < k and nums[k] == nums[k + 1]:
                k -= 1
        elif sum_of_triple < 0:
            j += 1
        else:
            k -= 1


print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(three_sum([0, 1, 1]))  # []
print(three_sum([0, 0, 0]))  # [[0,0,0]]
