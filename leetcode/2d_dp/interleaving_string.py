
# https://leetcode.com/problems/interleaving-string/description/

# Time Complexity: O(len(s1) × len(s2) × len(s3))
# Space Complexity: O(len(s1) × len(s2))
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    memo = {}

    def dfs(i, j, k):
        # base case
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        if (i, j) in memo:
            return memo[(i, j)]

        can_weave_left = can_weave_right = False

        # interleave left or right
        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            can_weave_left = dfs(i + 1, j, k + 1)

        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            can_weave_right = dfs(i, j + 1, k + 1)

        can_weave = can_weave_left or can_weave_right

        # only save to memo if its in bounds
        if i < len(s1) and j < len(s2):
            memo[(i, j)] = can_weave

        return can_weave

    return dfs(0, 0, 0)

print(is_interleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")) # True
print(is_interleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")) # False