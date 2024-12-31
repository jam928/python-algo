from collections import defaultdict
from typing import List

# https://leetcode.com/problems/diagonal-traverse/description/
# T: O(M * N)
# S: O(M * N)

def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    d = defaultdict(list)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            d[i + j].append(mat[i][j])

    ans = []

    for key, arr in d.items():
        if key % 2 == 0:
            ans.extend(arr[::-1])
        else:
            ans.extend(arr)

    return ans