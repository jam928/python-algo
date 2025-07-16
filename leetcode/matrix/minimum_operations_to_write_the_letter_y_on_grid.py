from typing import List

# T: O(N^2)
# S: O(1)
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:

        n = len(grid)
        center = n // 2

        yFreq = [0] * 3  # store freq of 0, 1, and 2 that lies on the Y
        nonYFreq = [0] * 3  # store freq of 0, 1, and 2 that does not lie on the Y

        totalY = 0  # total elements on Y
        totalNonY = 0

        for i in range(0, n):
            for j in range(0, n):
                if self.isOnY(n, center, i, j):
                    yFreq[grid[i][j]] += 1
                    totalY += 1
                else:
                    nonYFreq[grid[i][j]] += 1
                    totalNonY += 1

        # now that we have freq of all, we can try different combinations of y and non-y between 0,1,& 2.
        minOp = float('inf')

        for y in range(0, 3):
            for nonY in range(0, 3):
                if y == nonY:
                    continue

                yModifyCost = totalY - yFreq[y]  # cost of changing all items on Y to y
                nonYModifyCost = totalNonY - nonYFreq[nonY]  # cost of changing all items on NonY to nonY
                minOp = min(minOp, yModifyCost + nonYModifyCost)

        return minOp

    def isOnY(self, n, center, i, j):
        return (i == j and i <= center) or ((i + j + 1) == n and i <= center) or (i > center and j == center)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumOperationsToWriteY(grid = [[1,2,2],[1,1,0],[0,1,0]])) # 3
    print(s.minimumOperationsToWriteY(grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]])) # 12
