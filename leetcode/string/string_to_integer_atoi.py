# https://leetcode.com/problems/string-to-integer-atoi/
# T: O(N)
# S: O(N)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        op_found = False
        result = []
        for c in s:
            if c == '-' or c == '+':
                if op_found or len(result) != 0:
                    try:
                        return int(''.join(result))
                    except:
                        return 0
                op_found = True
                result.append(c)
            elif c.isdigit():
                result.append(c)
            else:
                break

        if len(result) == 0:
            return 0

        num = 0
        try:
            num = int(''.join(result))
        except:
            return 0

        if num < pow(2, 31) * -1:
            return pow(2, 31) * -1

        if num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        return num