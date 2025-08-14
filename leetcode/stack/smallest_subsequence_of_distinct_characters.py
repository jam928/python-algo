from collections import defaultdict

# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
# T: O(N)
# S: O(N)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurred = defaultdict(int)
        stack = []
        visited = set()

        # mark the last occured index for each character in s
        for i in range(len(s)):
            last_occurred[s[i]] = i

        for i in range(len(s)):
            if s[i] in visited:
                continue

            while stack and (stack[-1] > s[i]) and (last_occurred[stack[-1]] > i):
                visited.remove(stack.pop())

            stack.append(s[i])
            visited.add(s[i])

        return ''.join(stack)

if __name__ == '__main__':
    s = Solution()
    assert s.smallestSubsequence("bcabc") == "abc"
    assert s.smallestSubsequence("cbacdcbc") == "acdb"