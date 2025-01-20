from heapq import heappop, heappush
from typing import List

# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/

# T: O(n log n + mn log(mn))
# S: O(MN + N)
class Solution:
    def maxPoints(self, grid, qs: List[int]) -> List[int]:
        queries = sorted(set(qs))
        res = {}
        rows, cols = len(grid), len(grid[0])
        q = [(grid[0][0], 0, 0)] # heap
        prevCount = 0

        for num in queries:
            count = prevCount

            while q:
                val, r, c = q[0]

                if val >= num: break # pop only when the condition satisfy else break
                else:
                    heappop(q)
                    grid[r][c] = None
                    count += 1

                    for i, j in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                        if 0 <= i < rows and 0 <= j < cols and grid[i][j] is not None:
                            heappush(q, (grid[i][j], i, j))
                            grid[i][j] = None

            res[num] = prevCount = count

        ans = [res[num] for num in qs]
        return ans

if __name__ == '__main__':
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5, 6, 2]

    print(Solution().maxPoints(grid, queries)) # [5,8,1]

    grid = [[5, 2, 1], [1, 1, 2]]
    queries = [3]
    print(Solution().maxPoints(grid, queries)) # [0]