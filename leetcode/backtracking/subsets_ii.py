# https://leetcode.com/problems/subsets-ii/description/
from typing import List

# T: O(2^N)
# S: O(2^N)

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def subsets_helper(sub_list, start):
        # append sublist
        result.append(list(sub_list))

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            # append current number
            sub_list.append(nums[i])
            subsets_helper(sub_list, i + 1)
            # remove element when backtracking
            sub_list.pop()

    subsets_helper([], 0)

    return result

print(subsets_with_dup(nums = [1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(subsets_with_dup(nums = [0])) # [[],[0]]