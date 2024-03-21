
# https://leetcode.com/problems/edit-distance/description/

# T: O(nm) where n is the length of word1; where m is the length of word2
# S: O(nm) where n is the length of word1; where m is the length of word2
def min_distance(word1: str, word2: str) -> int:
    memo = {}

    def dfs(i, j):
        if i >= len(word1):
            return len(word2) - j  # if we went over the i ptr then return the remaining from len(word2) - j

        if j >= len(word2):
            return len(word1) - i  # if we went over the j ptr then return the remaining from len(word1) - i

        if (i, j) in memo:
            return memo[(i, j)]

        if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)

        # operations we are allowed to do in the string
        insert = 1 + dfs(i, j + 1)
        replace = 1 + dfs(i + 1, j + 1)
        delete = 1 + dfs(i + 1, j)

        min_operation = min(insert, replace, delete)
        memo[(i, j)] = min_operation
        return min_operation

    return dfs(0, 0)

print(min_distance(word1 = "horse", word2 = "ros")) # 3
print(min_distance(word1 = "intention", word2 = "execution")) # 5