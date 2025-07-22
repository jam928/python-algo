# T: O(LOGN)
# S: O(1)
# https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = pow(2, 31) - 1
        INT_MIN = pow(-2, 31)

        # to prevent overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        if divisor == 1:
            return dividend

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while dividend >= divisor:
            partial_quotient = 1
            temp_divisor = divisor

            # find the first half that (half + half) = dividend
            while temp_divisor + temp_divisor <= dividend:
                temp_divisor += temp_divisor
                partial_quotient += partial_quotient

            dividend -= temp_divisor
            quotient += partial_quotient

        return -quotient if negative else quotient

if __name__ == '__main__':

    s = Solution()
    assert s.divide(10, 3) == 3
    assert s.divide(7, -3) == -2
    assert s.divide(2147483647, 2) == 1073741823