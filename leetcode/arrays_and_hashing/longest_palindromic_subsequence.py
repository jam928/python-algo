# https://leetcode.com/problems/longest-palindromic-subsequence/

def longestPalindromeSubseq(s: str) -> int:
    dp = {}

    def helper(i, j):
        if i > j:
            return 0

        if i == j:
            return 1

        if (i, j) in dp:
            return dp[(i, j)]

        max_palindrome = 0
        if s[i] == s[j]:
            max_palindrome = 2 + helper(i + 1, j - 1)
        else:
            move_left = helper(i + 1, j)
            move_right = helper(i, j - 1)

            max_palindrome = max(max_palindrome, move_left, move_right)

        dp[(i, j)] = max_palindrome
        return max_palindrome

    return helper(0, len(s) - 1)

if __name__ == '__main__':
    print(longestPalindromeSubseq("bbbab")) # 4
    print(longestPalindromeSubseq("cbbd")) # 2