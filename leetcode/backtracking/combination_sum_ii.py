from typing import List

# https://leetcode.com/problems/combination-sum-ii/

# T: O(2^N)
# S: O(2^N)

def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    # sort the numbers to easily avoid duplicates
    candidates.sort()

    result = []

    # use a helper function
    def helper(current_list, current_sum, index):

        # if the target equals the current sum
        # add it to list
        if current_sum == target:
            result.append(list(current_list))
            return

        # if the current sum is greater than the target
        # return
        if current_sum > target:
            return

        # dfs with backtracking and avoid duplicates
        for i in range(index, len(candidates)):
            # avoid duplicates
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            current_list.append(candidates[i])
            helper(current_list, current_sum + candidates[i], i + 1)
            current_list.pop()

    helper([], 0, 0)

    return result

print(combination_sum_2(candidates = [10,1,2,7,6,1,5], target = 8))
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
print(combination_sum_2(candidates = [2,5,2,1,2], target = 5))
# [
# [1,2,2],
# [5]
# ]