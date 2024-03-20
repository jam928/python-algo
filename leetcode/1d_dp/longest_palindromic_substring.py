from typing import List

# T: O(n^2)
# S: O(1)

# https://leetcode.com/problems/longest-palindromic-substring/

class LongestPalindromicSubstring:
    def longest_palindrome(self, s: str) -> str:
        longest_palindrome = (0, 1)

        for i in range(1, len(s)):
            odd_palindrome = self.get_palindrome(s, i - 1, i + 1)
            even_palindrome = self.get_palindrome(s, i - 1, i)

            current_longest_palindrome = self.max_palindrome(odd_palindrome, even_palindrome)
            longest_palindrome = self.max_palindrome(longest_palindrome, current_longest_palindrome)

        return s[longest_palindrome[0]:longest_palindrome[1]]

    def get_palindrome(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return (i + 1, j)

    def max_palindrome(self, a, b):
        length_a = a[1] - a[0]
        length_b = b[1] - b[0]

        return a if length_a > length_b else b


if __name__ == '__main__':
    lps = LongestPalindromicSubstring()
    result = lps.longest_palindrome("babad") # aba
    print(result)

    result = lps.longest_palindrome("cbbd") # bb
    print(result)