class Solution:
    # Time: n/2 => O(N)
    # Space: O(1)
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                # here we can remove atmost one character and check where is it a palindrome - so as s[i] and s[j] are not same, we need to skip
                # CASE 1: either s[i] to do so we need to pass args as i+1, j,
                # CASE 2: or s[j] to do so we need to pass args as i, j-1
                return self.is_palindrome(s, i + 1, j) or self.is_palindrome(s, i, j - 1)
            i += 1
            j -= 1

        return True

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("deeee")) # true