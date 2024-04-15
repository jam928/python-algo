
# T: O(N)
# S: O(1)
# https://leetcode.com/problems/happy-number/
def is_happy(n: int) -> bool:
    slow = n
    fast = n
    while True:
        slow = calculate_sum(slow)  # move one step
        fast = calculate_sum(calculate_sum(fast))  # move two steps
        if slow == fast:
            break
    return slow == 1


def calculate_sum(num):
    sum_ = 0
    while num > 0:
        right = num % 10
        sum_ += right * right
        num //= 10
    return sum_


def is_happy2(n: int) -> bool:
    visited = set()

    result = False
    while True:
        if n == 1:
            result = True
            break
        n_str = str(n)
        n = 0
        for c in n_str:
            n += int(c) ** 2
        if n in visited:
            result = False
            break
        visited.add(n)

    return result
