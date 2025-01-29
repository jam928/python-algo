# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
# T: O(N)
# S: O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = i = 0
        count = [0, 0, 0]  # [a,b,c] count

        for j in range(len(s)):
            count[ord(s[j]) - ord('a')] += 1

            # shrink the window till it breaks constraint
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                count[ord(s[i]) - ord('a')] -= 1
                i += 1

            result += i

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubstrings("abcabc")) # 10
    print(s.numberOfSubstrings("aaacb")) # 3
    print(s.numberOfSubstrings("abc")) # 1