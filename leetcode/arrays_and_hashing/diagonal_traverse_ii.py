from collections import defaultdict
from typing import List

# https://leetcode.com/problems/diagonal-traverse-ii/
# T: O(N * M)
# S: O(N * M)

def find_diagonal_order(nums: List[List[int]]) -> List[int]:
    d = defaultdict(list)

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            d[i + j].append(nums[i][j])

    ans = []

    for key, arr in d.items():
        ans.extend(arr[::-1])

    return ans