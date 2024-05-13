from collections import defaultdict
from typing import List


# https://leetcode.com/problems/valid-sudoku/description/

def is_valid_sudoku(board: List[List[str]]) -> bool:
    # keep track of the elements in your row,columns, and square
    row_set = defaultdict(set)
    col_set = defaultdict(set)
    square_set = defaultdict(set)

    for row in range(9):
        for col in range(9):
            num = board[row][col]

            # if the current element is . then skip to the next one
            if "." == num:
                continue

            # if the current number is in the row set, column set, or square set
            # then we visited before thus violating the rules so return false
            if num in row_set[row] or num in col_set[col] or num in square_set[(row // 3, col // 3)]:
                return False

            # add the current number to the current row set, col set or square set
            row_set[row].add(num)
            col_set[col].add(num)
            square_set[(row // 3, col // 3)].add(num)

    return True


print(is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # true

print(is_valid_sudoku(board=
                      [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # false
