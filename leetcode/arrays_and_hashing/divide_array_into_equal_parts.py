from collections import Counter
from typing import List

# https://leetcode.com/problems/divide-array-into-equal-pairs
# T: O(N)
# S: O(N)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)

        for key, value in freq_map.items():
            if value % 2 != 0:
                return False
        
        return True
    
if __name__ == '__main__':
    s = Solution()
    assert s.divideArray([3,2,3,2,2,2]) == True
    assert s.divideArray([1,2,3,4]) == False