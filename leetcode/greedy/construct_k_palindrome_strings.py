from collections import Counter

# https://leetcode.com/problems/construct-k-palindrome-strings/description/
# T: O(N)
# S: O(N)

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k > len(s):
            return False

        # construct freq map from s
        freq_map = Counter(s)

        # if the number of odd freq is greater than k
        # then we cannot construct k palindrome strings
        for key in freq_map.keys():
            if freq_map[key] % 2 != 0:
                k -= 1

        return k >= 0

if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct("annabelle", 2)) # True
    print(s.canConstruct("leetcode", 3)) # False
    print(s.canConstruct("true", 4))  # True

