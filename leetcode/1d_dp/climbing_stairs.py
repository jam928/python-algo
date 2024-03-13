# https://leetcode.com/problems/climbing-stairs/

# T: O(n)
# S: O(n)

def climb_stairs(n: int) -> int:
    # fib seq in disguise
    fib = [0 for _ in range(n + 1)]

    fib[0] = 1
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
