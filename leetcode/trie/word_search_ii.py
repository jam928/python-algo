
# https://leetcode.com/problems/word-search-ii/description/
# T: O(k * L + (m*n) * 4 ^ L)
# S: O(k * L + L)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    def backtrack(node, i, j, path):
        char = board[i][j]
        if char not in node.children:
            return

        node = node.children[char]
        if node.is_end_of_word:
            result.add(path)

        board[i][j] = "#"  # Mark cell as visited
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != "#":
                backtrack(node, x, y, path + board[x][y])
        board[i][j] = char  # Backtrack

    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            backtrack(trie.root, i, j, board[i][j])
    return list(result)

print(find_words(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))
# ["eat", "oath"]
print(find_words(board = [["a","b"],["c","d"]], words = ["abcb"]))
# []
