from typing import List

# https://leetcode.com/problems/word-search/description/

# T: O(mn4^k) where k is the length of the word
# S: O(k) where k is the length of the word


def exist(board: List[List[str]], word: str) -> bool:
    def dfs(i, j, word_index):
        # if out of bounds
        # or current word index does not equal the current char in board exit
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word_index >= len(word) or word[word_index] != \
                board[i][j]:
            return False

        if word_index == len(word) - 1 and board[i][j] == word[word_index]:
            return True

        # backtrack and use temp char to avoid going over chars
        temp = board[i][j]
        board[i][j] = '#'
        result = dfs(i + 1, j, word_index + 1) or dfs(i - 1, j, word_index + 1) or dfs(i, j - 1, word_index + 1) or dfs(
            i, j + 1, word_index + 1)
        board[i][j] = temp

        return result

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) # True
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")) # True
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")) # False