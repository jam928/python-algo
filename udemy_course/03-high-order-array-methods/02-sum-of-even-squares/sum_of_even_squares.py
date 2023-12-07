def is_even(num):
    return num % 2 == 0


def sum_of_even_squares(numbers):
    return sum(num * num for num in filter(is_even, numbers))
