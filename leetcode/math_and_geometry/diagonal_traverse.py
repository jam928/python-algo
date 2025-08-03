from collections import defaultdict
from typing import List

# https://leetcode.com/problems/diagonal-traverse/
# T: O(MN)
# S: O(MN)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i + j].append(mat[i][j])

        ans = []

        for key, arr in d.items():
            if key % 2 == 0:
                arr.reverse()
            ans.extend(arr)

        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
    assert s.findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]