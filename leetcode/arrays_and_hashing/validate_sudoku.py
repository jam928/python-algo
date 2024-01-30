from typing import List

# https://leetcode.com/problems/valid-sudoku/description/

def is_valid_sudoku(board: List[List[str]]) -> bool:
    # validate the row does not have duplicates
    row_set = set()

    for i in range(len(board)):
        for j in range(len(board)):
            curr_cell = board[i][j]
            if curr_cell in row_set and curr_cell.isdigit():
                return False
            if curr_cell.isdigit():
                row_set.add(curr_cell)

        # reset the set for the next row
        row_set = set()

    # validate the column has no duplicates
    col_set = set()
    for j in range(len(board[0])):
        for i in range(len(board)):
            curr_cell = board[i][j]
            if curr_cell in col_set and curr_cell.isdigit():
                return False
            if curr_cell.isdigit():
                col_set.add(curr_cell)
        # Reset the set for the next column
        col_set = set()

    # validate if the 3x3 grid has duplicate
    row_index = 0
    col_index = 0

    while row_index < 9 and col_index < 9:
        s = set()
        for i in range(row_index, row_index + 3):
            for j in range(col_index, col_index + 3):
                curr_cell = board[i][j]
                if curr_cell in s and curr_cell.isdigit():
                    return False
                if curr_cell.isdigit():
                    s.add(curr_cell)

        col_index += 3
        if col_index >= 9:
            row_index += 3

            # reset the col index to 0 for the next set of rows
            col_index = 0

    return True

print(is_valid_sudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # true

print(is_valid_sudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # false