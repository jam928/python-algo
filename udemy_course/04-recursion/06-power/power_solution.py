def power(base, exponent):
    # Initialize result to 1
    result = 1

    # Multiply base by itself exponent times
    for i in range(exponent):
        result *= base

    return result


def power_2(base, exponent):
    # Base case - if exponent is 0, return 1
    if exponent == 0:
        return 1
    else:
        # Recursive case - return base multiplied by itself exponent - 1 times
        return base * power(base, exponent - 1)


def power_3(x, n):
    return 1 if n == 0 else x * power_3(x, n - 1)
