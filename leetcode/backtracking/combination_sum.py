from typing import List

# https://leetcode.com/problems/combination-sum/

# T: O(2^N)
# S: O(2^N)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(sub_list, current_sum, index):
            # if the current sum equals the target add it to result
            if current_sum == target:
                result.append(list(sub_list))
                return

            # if the current sum is greater than target then return since no other number will work either
            if current_sum > target:
                return

            # try all other possible combinations
            for i in range(index, len(candidates)):
                sub_list.append(candidates[i])
                helper(sub_list, candidates[i] + current_sum, i)
                sub_list.pop()  # pop last element to backtrack

        helper([], 0, 0)

        return result

if __name__ == '__main__':
    s = Solution()
    assert s.combinationSum(candidates = [2,3,6,7], target = 7) == [[2,2,3],[7]]
    assert s.combinationSum(candidates = [2,3,5], target = 8) == [[2,2,2,2],[2,3,3],[3,5]]
    assert s.combinationSum(candidates = [2], target = 1) == []
