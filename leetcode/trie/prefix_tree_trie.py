class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # iterate thru the string
        curr = self.root
        for c in word:
            # if the character is not in the current node add it to the children map
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # set the curr from the child
            curr = curr.children[c]

        # mark the current root as end
        curr.is_end = True

    # find the word in the trie
    # if one of the characters is not in the children map return None
    def find(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return None
            curr = curr.children[c]

        return curr

    # use the find method and if it returns a not null and its the end return True
    def search(self, word: str) -> bool:
        result = self.find(word)
        return result and result.is_end

    # use the find method and if it returns a not null return True
    def startsWith(self, prefix: str) -> bool:
        result = self.find(prefix)
        return result


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) # true
    print(trie.search("app")) # false
    print(trie.startsWith("app")) # true
    trie.insert("app")
    print(trie.search("app")) # True
