from typing import List

# https://leetcode.com/problems/word-break/
# T: O(n^2)
# S: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(word):
            if len(word) == 0:
                return True

            if word in memo:
                return memo[word]

            for i in range(1, len(word) + 1):
                current_word = word[0:i]
                if current_word in wordDict and dfs(word[i:]):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        return dfs(s)

if __name__ == '__main__':
    s = Solution()
    assert s.wordBreak(s="leetcode", wordDict=["leet", "code"]) == True
    assert s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]) == True
    assert s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) == False
