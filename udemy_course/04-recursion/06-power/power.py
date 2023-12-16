def power(base: float, exponent: float) -> float:
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)