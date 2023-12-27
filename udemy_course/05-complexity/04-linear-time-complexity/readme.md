# Linear Time Complexity `O(n)`

We have established that linear time complexity is when the runtime scales linearly with the input. As the input size increases, the runtime of the algorithm also increases in a linear fashion. This behavior is denoted by Big O notation as O(n), where n represents the size of the input.

Let's look at an example of a linear time O(n) function.

```python
def sum_array(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    return sum
```

This function takes in an array and adds the numbers together. For each number in the array, it will run one step. If the array has 2 number, it will run 2 steps. If the array has 1 million numbers, it will run 1 million steps, which obviously takes longer.

Let's try it out.

```python
import time


def sum_array(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    return sum


arr1 = [1, 2, 3, 4, 5]
start = time.time()
print(sum_array(arr1))
end = time.time()
print(f"Sum array1 took: {end - start} ms")

arr2 = list(range(1, 10000000))
start = time.time()
print(sum_array(arr2))
end = time.time()
print(f"Sum array2 took: {end - start} ms")

```

In `Sum Array 1`, we have an array with 5 numbers. In `Sum Array 2`, we have an array with 10,000 numbers. Let's run this code and see how long it takes.

Your results will be different, but I get the following:

```python
# 15
# Sum array1 took: 0.0 ms
# 49999995000000
# Sum array2 took: 0.3962998390197754 ms
```

So a huge jump there.

This is an example of linear time complexity. The runtime scales linearly with the input.

Most of the challenges that we have done are `O(n)` because they have to iterate over the input.

Even something like this:

```python
def reverse_string(str):
    reverse_str = ""

    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]

    return reverse_str
```

is `O(n)` because it has to iterate over the string. We did not write a loop, but the `split`, `reverse`, and `join` methods all have to iterate over the string.

There are other complexities that we will look at later, but for now, we will focus on `O(1)` and `O(n)`.

## Dice Game Complexity

Remember the dice game that we made? Let's look at the complexity of that. Here is the function:

```python
import random


def dice_game_simulation(num_simulations):
    simulations_result = []

    for i in range(num_simulations):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum = dice_1 + dice_2

        result = "roll again"

        if sum == 7 or sum == 11:
            result = 'win'
        elif sum == 2 or sum == 3 or sum == 12:
            result = 'lose'

        simulations_result.append({"dice1": dice_1, "dice2": dice_2, "sum": sum, "result": result})

    return simulations_result

```

This function has a few different parts. Let's look at each one.

```python
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
```

This function is `O(1)` because it does not depend on the input. It will always run in the same amount of time.

```python
        sum = dice_1 + dice_2

        result = "roll again"

        if sum == 7 or sum == 11:
            result = 'win'
        elif sum == 2 or sum == 3 or sum == 12:
            result = 'lose'
```

This part is also `O(1)` because it does not depend on the input. It will always run in the same amount of time.

```python
for i in range(num_simulations):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum = dice_1 + dice_2

        result = "roll again"

        if sum == 7 or sum == 11:
            result = 'win'
        elif sum == 2 or sum == 3 or sum == 12:
            result = 'lose'

        simulations_result.append({"dice1": dice_1, "dice2": dice_2, "sum": sum, "result": result})

    return simulations_result
```

This part is `O(n)` because it depends on the input. The more times the loop runs, the longer it will take.

So the overall complexity of the function is `O(n)` because the `O(1)` parts are insignificant compared to the `O(n)` part.
