# https://leetcode.com/problems/reverse-integer/description/
# T: O(LOGN)
# S: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = pow(-2, 31)
        INT_MAX = pow(2, 31) - 1

        reversed_num = 0
        while x != 0:
            digit = x % 10 if x > 0 else x % -10
            reversed_num = reversed_num * 10 + digit
            x = int(x / 10)

        return reversed_num if INT_MIN < reversed_num < INT_MAX else 0

if __name__ == "__main__":
    s = Solution()

    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21