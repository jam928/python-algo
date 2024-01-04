# Logarithmic Time Complexity `O(log n)`

Logarithmic time complexity is when the runtime grows logarithmically with the input size. As the input size increases, the runtime of the algorithm increases, but at a much slower rate compared to linear or quadratic time complexities. In a logarithmic time algorithm, the number of operations scales logarithmically with the input size.

Logarithmic time complexity is denoted by Big O notation as O(log n) or "O of log n", where n represents the size of the input.

## Example: Logarithmic Time Complexity Function

Consider a function called `find_power` that calculates the power of a number using recursion. The function takes two parameters:

- `base` - the base number.
- `exponent` - the exponent to which the base is raised.

We will be using recursion in this example, which we learned about in the last section.

```python
def find_power(base, exponent):
    if exponent == 0:
        return 1

    if (base, exponent) in mem_cache:
        return mem_cache.get((base, exponent))

    if exponent % 2 == 0:
        half_power = find_power(base, exponent // 2)
        result = half_power * half_power
        mem_cache.update({(base, exponent): result})
        return result

    half_power = find_power(base, (exponent - 1) // 2)
    result = base * half_power * half_power
    mem_cache.update({(base, exponent): result})
    return result
```

In the `find_power` function, we use recursion to efficiently calculate the power of a number. The function exploits the property that any number raised to an even exponent can be split into two halves, and the result is the square of the number raised to half the exponent. For odd exponents, the function reduces the exponent by 1 and repeats the process.

## Efficiency and Best Use Cases

Logarithmic time complexity is highly efficient and desirable for large datasets or problems that can be divided into smaller sub-problems. It is often encountered in algorithms that utilize divide-and-conquer strategies or binary search, which we will talk about soon when we get to data structures and algorithms.

In the example of `find_power`, the algorithm efficiently computes the power of a number by reducing the number of multiplications required, making it ideal for calculations with large exponents.

## Testing the Runtime

Testing the runtime of logarithmic time algorithms can be done with larger input sizes and observing the relatively slow growth of runtime compared to linear or quadratic algorithms. However, keep in mind that logarithmic time algorithms are already highly efficient, and the difference in runtime for moderately large input sizes may not be significant.

Try running this code:

```python
start = time.time()
print(find_power(2, 100))
end = time.time()
print(f"Find power 1 took: {end - start} ms")

start = time.time()
mem_cache = {}
print(find_power(2, 1000000))
end = time.time()
print(f"Find power 2 took: {end - start} ms")
```

The result that I got is:

```sh
Find Power 1: 0.048ms
Find Power 2: 0.005ms
```

The runtime for `find_power` with an exponent of 1 billion is slightly faster than the runtime for an exponent of 100. This is because the algorithm is already highly efficient, and the difference in runtime is not significant. Remember, there are many other factors that can affect the runtime of an algorithm, such as the hardware and software environment.
