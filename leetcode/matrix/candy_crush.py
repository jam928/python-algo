from typing import List

# https://leetcode.com/problems/candy-crush/
# T: O((MN) ^ 2)
# S: O(1)

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])

        found = True

        while found:
            found = False

            # check rows or cols if all have same value
            for i in range(m):
                for j in range(n):
                    val = abs(board[i][j])
                    if val == 0:
                        continue
                    # check if the current value is the same across the whole current row
                    if j < n - 2 and abs(board[i][j + 1]) == val and abs(board[i][j + 2]) == val:
                        found = True
                        col_index = j
                        # set all values to negative
                        while col_index < n and abs(board[i][col_index]) == val:
                            board[i][col_index] = -val
                            col_index += 1

                    # check if the current value is the same across the whole current col
                    if i < m - 2 and abs(board[i + 1][j]) == val and abs(board[i + 2][j]) == val:
                        found = True
                        row_index = i
                        # set all values to negative for this col
                        while row_index < m and abs(board[row_index][j]) == val:
                            board[row_index][j] = -val
                            row_index += 1

            if found:  # move positive values to the bottom, then set the rest to 0
                for j in range(n):
                    storeIndex = m - 1
                    for i in range(m - 1, -1, -1):
                        if board[i][j] > 0:
                            board[storeIndex][j] = board[i][j]
                            storeIndex -= 1

                    for k in range(storeIndex, -1, -1):
                        board[k][j] = 0

        return board

if __name__ == "__main__":
    s = Solution()
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [210, 0, 0, 0, 214], [310, 0, 0, 113, 314], [410, 0, 0, 213, 414], [610, 211, 112, 313, 614], [710, 311, 412, 613, 714], [810, 411, 512, 713, 1014]]
    print(s.candyCrush(board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))

    print(s.candyCrush(board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]))
    # [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
