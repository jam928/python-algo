
# https://leetcode.com/problems/count-and-say/
# T: O(2^N)
# S: O(2^N)

class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"

        s = self.countAndSay(n - 1)
        result = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1  # reset count

        if count != 0:
            result.append(str(count) + s[len(s) - 1])
        return ''.join(result)

if __name__ == '__main__':
    s = Solution()
    assert s.countAndSay(4) == "1211"
    assert s.countAndSay(1) == "1"