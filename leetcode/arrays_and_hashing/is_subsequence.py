# https://leetcode.com/problems/is-subsequence/description/

# If the length of s is greater than the length of t then return false
def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False

    # 2 ptr approach
    # Iterate through the t string and move the i pointer only if it equals the current char at j in the t string
    # Return true if i equals the length of the s string; means we traversed thru the whole s string
    i = 0
    j = 0

    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


print(is_subsequence("abc", "ahbgdc"))  # true
print(is_subsequence("axc", "ahbgdc"))  # false
