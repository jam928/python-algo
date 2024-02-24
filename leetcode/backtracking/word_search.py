from typing import List

# https://leetcode.com/problems/word-search/description/

# T: O(mn4^k) where k is the length of the word
# S: O(k) where k is the length of the word


def exist(board: List[List[str]], word: str) -> bool:
    result = [False]

    def validate_word(i, j, index):
        # return if out of bounds or if its a bad character
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] == '#' or index >= len(word) or \
                board[i][j] != word[index]:
            return

            # add to result list if the current word equals the word
        if index == len(word) - 1:
            result[0] = True
            return

        # backtrack
        temp = board[i][j]
        board[i][j] = '#'

        validate_word(i + 1, j, index + 1)
        validate_word(i - 1, j, index + 1)
        validate_word(i, j + 1, index + 1)
        validate_word(i, j - 1, index + 1)

        board[i][j] = temp

    # iterate through each cell and check if the cell letter matches the first letter in word
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                validate_word(i, j, 0)
                if result[0]:
                    break

    return result[0]

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) # True
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")) # True
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")) # False