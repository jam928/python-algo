class Solution:
    def __init__(self):
        self.result = 0

    def maxProduct(self, s: str) -> int:
        self.result = 0
        s1 = s2 = ""
        self.dfs(s, 0, s1, s2)
        return self.result

    def dfs(self, s, i, s1, s2):
        if i >= len(s):
            if self.is_palindrome(s1) and self.is_palindrome(s2):
                self.result = max(self.result, len(s1) * len(s2))
            return

        # include current character in s1
        self.dfs(s, i + 1, s1 + s[i], s2)

        # include current character in s2
        self.dfs(s, i + 1, s1, s2 + s[i])

        # Exclude current character from both s1 and s2
        self.dfs(s, i + 1, s1, s2)

    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct("leetcodecom")) # 9
    print(solution.maxProduct("bb")) # 1
    print(solution.maxProduct("accbcaxxcxx")) # 25