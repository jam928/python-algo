from typing import List

# https://leetcode.com/problems/word-search/description/

# T: O(mn4^k) where k is the length of the word
# S: O(k) where k is the length of the word


def exist(board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and verify(i, j, 0, board, word):
                return True

    return False

def verify(i, j, index, board, word):
    if i < 0 or \
            i >= len(board) or \
            j < 0 or \
            j >= len(board[0]) or \
            index >= len(word) or \
            board[i][j] != word[index]:
        return False

    if index == len(word) - 1 and board[i][j] == word[len(word) - 1]:
        return True

    result = False
    temp = board[i][j]
    board[i][j] = '#'
    if verify(i - 1, j, index + 1, board, word) or \
            verify(i + 1, j, index + 1, board, word) or \
            verify(i, j - 1, index + 1, board, word) or \
            verify(i, j + 1, index + 1, board, word):
        result = True
    board[i][j] = temp
    return result

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) # True
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")) # True
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")) # False