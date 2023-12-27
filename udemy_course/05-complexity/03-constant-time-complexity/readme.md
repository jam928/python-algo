# Constant Time Complexity `O(1)`

We have established that `constant` time complexity is when the runtime is always the same, no matter how big the input is. `Linear` time complexity is when the runtime scales linearly with the input. To describe this in Big O notation, we use `O(1)` (pronounced "O of 1" or "big O of 1").

Let's look at an example of a constant time O(1) function.

```python
def access_element(arr, index):
    return arr[index]
```

This function takes in an array and an index and returns the element at that index. No matter how big the array is, the runtime will always be the same because it is only doing one operation. We can describe this function as `O(1)` in Big O notation.

```python
import timeit

def access_element(arr, index):
    return arr[index]


arr1 = [1, 2, 3, 4, 5]
time1 = timeit.timeit(lambda: access_element(arr1, 1), number=100000)
print("Access Element 1:", time1)

arr2 = list(range(1, 10001))
time2 = timeit.timeit(lambda: access_element(arr2, 1), number=100000)
print("Access Element 2:", time2)


```

With the `timeit.timeit` function, we can see how long it takes to run the code between them.

`Access Element 1` passes in an array with 5 elements and `Access Element 2` passes in an array with 10,000 elements.

All of you will get a different result. As I said in the last lesson, there are so many factors including your computer, your operating system, and what other programs you have running. Also, the way that your computer allocates memory can affect the runtime. The one truth is that if you increase the size of the array, the runtime will still stay in the same general range.

Change the length of the array in `Access Element 2` to 100,000 and run the code again.

```python
arr2 = list(range(1, 10001))
time2 = timeit.timeit(lambda: access_element(arr2, 1), number=100000)
print("Access Element 2:", time2)
```

You should see that the runtime is still in the same general range.
