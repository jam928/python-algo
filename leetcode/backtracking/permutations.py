# https://leetcode.com/problems/permutations/description/
from typing import List

# T:O(N!)
# S:O(N!)
def permute(nums: List[int]) -> List[List[int]]:
    # use helper to recursively add lists via backtracking
    result = []

    def helper(current_list):
        # if the length of nums equals length of current list add it to the result
        if len(nums) == len(current_list):
            result.append(list(current_list))
            return

        # append current number in iteration to list
        # do recursive call till we reach the end
        # backtrack for other possible combinations
        for num in nums:
            # don't do recursively call helper if the current number is in the list already
            if num in current_list:
                continue
            current_list.append(num)
            helper(current_list)
            current_list.pop()

    helper([])

    return result

print(permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute([0,1])) # [[0,1],[1,0]]
print(permute([1])) # [[1]]
