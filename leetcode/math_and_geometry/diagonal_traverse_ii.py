from collections import defaultdict
from typing import List

# https://leetcode.com/problems/diagonal-traverse-ii/
# T: O(MN)
# S: O(MN)

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i + j].append(nums[i][j])

        ans = []

        for key, arr in d.items():
            arr.reverse()
            ans.extend(arr)

        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,4,2,7,5,3,8,6,9]
    assert s.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]) == [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
