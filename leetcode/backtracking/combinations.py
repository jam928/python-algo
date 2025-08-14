from typing import List

# https://leetcode.com/problems/combinations/
# T: O(K * (N choose K))
# S: O(K * (N choose K))

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def helper(current_list, k, i):
            if k == 0:
                result.append(list(current_list))
                return

            for index in range(i, n + 1):
                current_list.append(index)
                helper(current_list, k - 1, index + 1)
                current_list.pop()

        helper([], k, 1)
        return result

if __name__ == '__main__':
    s = Solution()
    assert s.combine(4, 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert s.combine(1,1) == [[1]]