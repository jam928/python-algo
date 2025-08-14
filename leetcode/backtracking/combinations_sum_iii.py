from typing import List


# https://leetcode.com/problems/combination-sum-iii/
# T: O(K (9 Choose K))
# S: O(K (9 Choose K))
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def helper(current_list, k, i, current_sum):
            if k == 0 and current_sum == n:
                result.append(list(current_list))
                return

            # if we ran out of k numbers and N is not zero return
            if k == 0 and n != 0:
                return

            for index in range(i, 9 + 1):
                if index > n:
                    break
                current_list.append(index)
                helper(current_list, k - 1, index + 1, current_sum + index)
                current_list.pop()

        helper([], k, 1, 0)
        return result