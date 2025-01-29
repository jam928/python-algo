from collections import deque

# https://leetcode.com/problems/decode-string/

# T: O(N * K) where k is the max repeated counted
# T: O(N + D) where d is the depth of the max brackets
class Solution:
    """
        1. Convert letters in string to a queue
        2. DFS decode string
        2a. convert number to string
        2b. if starts with [ dfs and get the result and repeat number times from the 2a and then reset num
        2c. ] then break out of for loop and return
        2d. append to string
    """

    def decodeString(self, s: str) -> str:
        q = deque()

        for c in s:
            q.append(c)

        def helper(q):
            arr = []
            num = ""

            while q:
                c = q.popleft()

                if c.isdigit():
                    num = num + c
                elif c == '[':
                    sub = helper(q)
                    arr.append(sub * int(num))
                    num = ""
                elif c == ']':
                    break
                else:
                    arr.append(c)

            return ''.join(arr)

        return helper(q)

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]")) # aaabcbc
    print(s.decodeString("3[a2[c]]")) # accaccacc
    print(s.decodeString("2[abc]3[cd]ef")) # abcabccdcdcdef