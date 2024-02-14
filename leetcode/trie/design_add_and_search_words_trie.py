
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # iterate the word
        curr = self.root

        for c in word:
            # if the character is not in the current node add it to the children map
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        # mark the current last node as end true
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        return self.searchHelper(curr, word)

    def searchHelper(self, curr, word):
        for i in range(len(word)):
            ch = word[i]

            if ch not in curr.children:
                # if its the wild character try the characters in the map recursively
                if ch == '.':
                    for c, child in curr.children.items():
                        if self.searchHelper(child, word[i + 1:]):
                            return True
                return False
            else:
                curr = curr.children[ch]

        return curr.is_end


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # return False
    print(wordDictionary.search("bad"))  # return True
    print(wordDictionary.search(".ad"))  # return True
    print(wordDictionary.search("b.."))  # return True