from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    memo = {}

    def dfs(word):
        if len(word) == 0:
            return True

        if word in memo:
            return memo[word]

        for i in range(1, len(word) + 1):
            current_word = word[0:i]
            if current_word in word_dict and dfs(word[i:]):
                memo[word] = True
                return True
        memo[word] = False
        return False

    return dfs(s)


print(word_break(s="leetcode", word_dict=["leet", "code"])) # true
print(word_break(s="applepenapple", word_dict=["apple", "pen"])) # true
print(word_break(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"])) # false
