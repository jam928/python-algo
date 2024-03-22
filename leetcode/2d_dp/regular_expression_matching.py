def is_match(self, s: str, p: str) -> bool:
    memo = {}

    def helper(i, j):
        # if we exhausted both strings then return true
        if i >= len(s) and j >= len(p):
            return True

        # if we only exhausted the pattern string return False
        if j >= len(p):
            return False

        if (i, j) in memo:
            return memo[(i, j)]

        matched = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if ((j + 1) < len(p) and p[j + 1] == '*'):
            is_match = helper(i, j + 2) or (matched and helper(i + 1, j))
            memo[(i, j)] = is_match
            return memo[(i, j)]

        if matched:
            is_matched = helper(i + 1, j + 1)
            memo[(i, j)] = is_matched
            return is_matched
        memo[(i, j)] = False
        return memo[(i, j)]

    return helper(0, 0)
