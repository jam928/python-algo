from collections import defaultdict
from typing import List

# https://leetcode.com/problems/sudoku-solver/
# T: O(9^N)
# S: O(1)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.num_row_map = defaultdict(set)
        self.num_col_map = defaultdict(set)
        self.num_sub_sq_map = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                self.num_row_map[i].add(num)
                self.num_col_map[j].add(num)
                self.num_sub_sq_map[(i // 3, j // 3)].add(num)

        self.dfs(0, 0, board)

    def dfs(self, i, j, board):
        if i == 9:
            return True

        if board[i][j] != '.':
            return self.dfs(i, j + 1, board) if j + 1 < 9 else self.dfs(i + 1, 0,
                                                                        board)  # try the next col or go to the next row

        for num in "123456789":
            sub_square = (i // 3, j // 3)

            if num in self.num_row_map[i] or num in self.num_col_map[j] or num in self.num_sub_sq_map[(i // 3, j // 3)]:
                continue

            board[i][j] = num
            self.num_row_map[i].add(num)
            self.num_col_map[j].add(num)
            self.num_sub_sq_map[(i // 3, j // 3)].add(num)

            res = self.dfs(i, j + 1, board) if j + 1 < 9 else self.dfs(i + 1, 0,
                                                                       board)  # try the next col or go to the next row

            if res:
                return True

            board[i][j] = '.'

            # backtrack
            self.num_row_map[i].remove(num)
            self.num_col_map[j].remove(num)
            self.num_sub_sq_map[(i // 3, j // 3)].remove(num)

        return False

if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
    assert board == [["5","3","4","6","7","8","9","1","2"],
                     ["6","7","2","1","9","5","3","4","8"],
                     ["1","9","8","3","4","2","5","6","7"],
                     ["8","5","9","7","6","1","4","2","3"],
                     ["4","2","6","8","5","3","7","9","1"],
                     ["7","1","3","9","2","4","8","5","6"],
                     ["9","6","1","5","3","7","2","8","4"],
                     ["2","8","7","4","1","9","6","3","5"],
                     ["3","4","5","2","8","6","1","7","9"]]

