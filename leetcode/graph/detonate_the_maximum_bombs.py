import collections
from typing import List


# T: O(N^2)
# S: O(N^2)
# https://leetcode.com/problems/detonate-the-maximum-bombs/description/

def maximum_detonation(bombs: List[List[int]]) -> int:
    bomb_map = collections.defaultdict(set)
    n = len(bombs)

    for i in range(n):  # i is source
        x1, y1, r1 = bombs[i]

        for j in range(n):
            if i == j: continue

            x2, y2, r2 = bombs[j]

            if r1 ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:  # reachable from i
                bomb_map[i].add(j)

    def dfs(n):  # return None
        if n in seen: return
        seen.add(n)
        for neighbor in bomb_map[n]:
            dfs(neighbor)

    ans = 0
    for i in range(n):
        seen = set()
        dfs(i)
        ans = max(ans, len(seen))
    return ans


print(maximum_detonation(bombs=[[2, 1, 3], [6, 1, 4]]))  # 2
print(maximum_detonation(bombs=[[1, 1, 5], [10, 10, 5]]))  # 1
print(maximum_detonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))  # 5
