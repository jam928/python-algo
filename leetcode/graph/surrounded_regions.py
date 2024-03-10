from typing import List

# T: O(m * n)
# S: O(m * n)

# https://leetcode.com/problems/surrounded-regions/

def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            # dfs all border o's and its connected components
            on_border = True if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1 else False
            if board[i][j] == 'O' and on_border:
                dfs(board, i, j)

    # Convert all o's that were not affected by the border to X
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '#':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'


def dfs(board, i, j):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != 'O':
        return

    board[i][j] = '#'
    dfs(board, i - 1, j)
    dfs(board, i + 1, j)
    dfs(board, i, j + 1)
    dfs(board, i, j - 1)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
print(board)

board = [['X']]
solve(board)
print(board)