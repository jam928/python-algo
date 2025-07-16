from typing import List

# https://leetcode.com/problems/count-sub-islands/description/?envType=company&envId=doordash&favoriteSlug=doordash-all
# T: O(MN)
# S: O(MN)

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if grid1[i][j] != 1:
                return 0

            grid2[i][j] = mark  # Mark as visited

            is_sub_island = 1

            for dx, dy in moves:
                # if out of bounds of grid or the next neighbor is not 1 continue
                if 0 > dx + i or dx + i >= rows or 0 > dy + j or dy + j >= cols or grid2[dx + i][dy + j] != 1:
                    continue

                # if the next neighbor is a 1 in grid2 but not grid 1 return 0
                if grid1[dx + i][dy + j] != 1:
                    is_sub_island = 0

                if dfs(dx + i, dy + j) == 0:
                    is_sub_island = 0

            return is_sub_island

        rows = len(grid1)
        cols = len(grid1[0])

        count = 0
        mark = 2

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    count += dfs(i, j)
                    mark += 1

        return count

if __name__ == '__main__':
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(Solution().countSubIslands(grid1, grid2)) # 2

