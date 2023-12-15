def fibonacci(num: int) -> int:
    if num < 2:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_2(num):
    return num if num < 2 else fibonacci(num - 1) + fibonacci(num - 2)
