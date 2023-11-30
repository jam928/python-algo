# Challenge: FizzBuzz Array

## Instructions

FizzBuzz is probably the most common interview question for entry level developers. At least, it used to be. It may not be used as much because of how common it was. It's a simple problem that tests your ability to think logically and write clean code.

Traditionally, you loop from 1 to 100 and print out each number. However, if the number is divisible by 3, you print out "Fizz" instead. If the number is divisible by 5, you print out "Buzz" instead. If the number is divisible by both 3 and 5, you print out "FizzBuzz" instead.

In this challenge, you will write a function called `fizz_buzz_array` that takes in a number and returns an array. The array should contain all the numbers from 1 to the number passed in. However, if the number is divisible by 3, you should replace the number with "Fizz". If the number is divisible by 5, you should replace the number with "Buzz". If the number is divisible by both 3 and 5, you should replace the number with "FizzBuzz".

### Function Signature

```python
def fizz_buzz_array(num: int) -> any[]:
    """
    Returns the array of numbers.
    
    Parameters:
    - num (int):  The number to loop up to.
    """
```


### Examples

```python
fizz_buzz_array(5) # [1, 2, "Fizz", 4, "Buzz"]
fizz_buzz_array(15) # [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
```

### Constraints

- The number passed in will always be greater than 0
- The number passed in will always be an integer

### Hints

- Instead of console logging each number, you will need to push each number into an array.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def fizz_buzz_array(num):
    # Store the resulting fizzbuzz elements
    result = []
    for i in range(1, num+1):
        # if the current element is divisible both by 3 and 5 then append fizzbuzz
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # else if the current element is divisible both by 3 only append fizz
        elif i % 3 == 0:
            result.append("Fizz")
        # else if the current element is divisible both by 5 only append buzz
        elif i % 5 == 0:
            result.append("Buzz")
        # else append the current element
        else:
            result.append(i)

    return result
```

### Explanation

- Create an empty array to store our results.
- Loop from 1 to the number passed in.
- Check if the number is divisible by both 3 and 5 first. If it is, we push "FizzBuzz" into the array.
- If it's not, we check if the number is divisible by 3. If it is, we push "Fizz" into the array.
- If it's not, we check if the number is divisible by 5. If it is, we push "Buzz" into the array.
- If it's not, we push the number into the array.
- Return the array.

</details>

### Test Cases

```python
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

```
