import fizzbuzz_array as fa


def test_fizz_buzz_array():
    assert fa.fizz_buzz_array(15) == [
        1,
        2,
        'Fizz',
        4,
        'Buzz',
        'Fizz',
        7,
        8,
        'Fizz',
        'Buzz',
        11,
        'Fizz',
        13,
        14,
        'FizzBuzz',
    ]
