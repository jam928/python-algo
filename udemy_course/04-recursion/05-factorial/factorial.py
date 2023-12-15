def factorial(num: int) -> int:
    if num <= 1:
        return 1

    return num * factorial(num - 1)


def factorial_2(num: int) -> int:
    return 1 if num <= 1 else num * factorial(num - 1)
