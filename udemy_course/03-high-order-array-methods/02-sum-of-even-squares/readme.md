# Challenge: Sum of Squares of Even Numbers

## Instructions

Let's start off with a fairly simple challenge, but one that uses a few different array methods. Write a function called `sum_of_even_squares` that takes an array of numbers and returns the sum of the squares of the even numbers in the array.

### Function Signature

```python
def sum_of_even_squares(numbers):
    """
    Returns the sum of the squares of the even numbers in the array.
    :param numbers: The array of numbers.
    :type numbers: list of int
    :return: The sum of the squares of even numbers.
    :rtype: int
    """
```

### Examples

```python
sum_of_even_squares([1, 2, 3, 4, 5]) # 20 (2^2 + 4^2)
sum_of_even_squares([-1, 0, 1, 2, 3, 4]); # 20 (0^2 + 2^2 + 4^2)
sum_of_even_squares([]); # 0
```

### Hints

- Use the `filter` method to select the even numbers from the array.
- Use the `sum` method to sum up the squared even numbers.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def is_even(num):
    return num % 2 == 0


def sum_of_even_squares(numbers):
    return sum(num * num for num in filter(is_even, numbers))
```

### Explanation

You can format this so many different ways. This is just one example.

- Call `sum` method and in it pass the operation we want to do first for each number; in this case num * num, and then it will be filter based on the latter code

- For the `filter` method, pass in a callback function that takes in a number and returns `true` if the number is even and `false` otherwise. We used the modulo operator (`%`) to check if the number is even.

</details>

### Test Cases

```python
import sum_of_even_squares as s


def test_sum_of_even_squares():
    assert s.sum_of_even_squares([1, 2, 3, 4, 5]) == 20
    assert s.sum_of_even_squares([-1, 0, 1, 2, 3, 4]) == 20
    assert s.sum_of_even_squares([]) == 0
```
