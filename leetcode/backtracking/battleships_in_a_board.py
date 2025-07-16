from typing import List

# https://leetcode.com/problems/battleships-in-a-board/description/
# T: O(MN)
# S: O(M) or O(N)

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'X':
                return

            temp = board[i][j]
            board[i][j] = 'x'

            dfs(i + 1, j)
            dfs(i, j + 1)

        count = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "X":
                    dfs(i, j)
                    count += 1

        return count

if __name__ == '__main__':
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    print(Solution().countBattleships(board)) # 2

    board = [["."]]
    print(Solution().countBattleships(board)) # 0
