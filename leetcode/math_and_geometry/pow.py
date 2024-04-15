# T: O(logN)
# S: O(logN)
# https://leetcode.com/problems/powx-n/

def my_pow(x: float, n: int) -> float:
    def helper(n):
        if n == 0:
            return 1

        if x == 0:
            return 0

        # divide and conquer approach 2^5 * 2^5
        res = helper(n // 2)
        res = res * res

        # include res * x if n is odd
        return res if n % 2 == 0 else res * x

    result = helper(abs(n))
    return result if n >= 0 else (1 / result)

print(my_pow(x = 2.00000, n = 10)) # 1024.00000
print(my_pow(x = 2.10000, n = 3)) # 9.26100
print(my_pow(x = 2.00000, n = -2)) # 0.25