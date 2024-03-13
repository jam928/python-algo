# T: O(n)
# S: O(n)
# https://leetcode.com/problems/decode-ways/
def num_decodings(s: str) -> int:
    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]

        if i < len(s) and s[i] == '0':
            return 0

        if i >= len(s) - 1:
            return 1

        count = helper(i + 1)

        if int(s[i:i + 2]) <= 26:
            count += helper(i + 2)

        memo[i] = count
        return count

    return helper(0)
