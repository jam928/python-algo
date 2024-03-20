# T: O(n^2)
# S: O(1)

# https://leetcode.com/problems/palindromic-substrings/description/

def count_substrings(s: str) -> int:
    count = 0

    for i in range(1, len(s)):
        count += get_palindrome(s, i - 1, i + 1)  # count for the odd palindrome
        count += get_palindrome(s, i - 1, i)  # count for the even palindrome

    return count + len(s)  # count for the palindrome plus the length of the string


def get_palindrome(s, i, j):
    count = 0
    while i >= 0 and j < len(s):
        if s[i] != s[j]:
            break
        count += 1
        i -= 1
        j += 1
    return count

print(count_substrings(s = "abc")) # 3
print(count_substrings(s = "aaa")) # 6