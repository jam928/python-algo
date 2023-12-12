# Unwinding

We talked about the basics of recursion and looked at a simple example in the last lesson. In this lesson, I want to look at a key concept in recursion called "unwinding".

We know that when we run a function recursively, it calls itself until it reaches a base case. After it reaches that base is when it starts returning values as it "unwinds" the recursion. The order in which the function calls are returned is the reverse order of the function calls. This is because the function calls are added to the call stack, which is a LIFO (last in, first out) data structure.

We're actually going to look at stacks and other data structures later. In fact we will create our own implementation of a stack. I do want to explain the basics now though so that you can understand how recursion and unwinding work.

Let's look at an example of this. Consider the following function:

```python
def sum_up_to(n):

    if(n == 1):
        return 1
    
    return n + sum_up_to(n-1)
```

This function uses recursion to calculate the sum of positive integers up to `n`. For example, if the input is 5, the function should return 15 (1 + 2 + 3 + 4 + 5).

Let's see how this function works. When we call `sum_up_to(5)`, it executes `sum_up_to(4) + 5`. Now, `sum_up_to(4)` calls `sum_up_to(3) + 4`. Continuing, `sum_up_to(3)` calls `sum_up_to(2) + 3`. In the next call, `sum_up_to(2)` calls `sum_up_to(1) + 2`. Finally, `sum_up_to(1)` returns 1.

Now, we can start "unwinding" the recursion and adding the numbers to form the sum:

```python
sum_up_to(1) returns 1
sum_up_to(2) returns 1 + 2 = 3
sum_up_to(3) returns 1 + 2 + 3 = 6
sum_up_to(4) returns 1 + 2 + 3 + 4 = 10
sum_up_to(5) returns 1 + 2 + 3 + 4 + 5 = 15
```

As you can see, the function starts returning values as it "unwinds" the recursion. It returns in the reverse order of the function calls, which is why it's called "unwinding".

## A Look At The Call Stack

As I said above, the call stack is a LIFO (last in, first out) data structure, which means that the last function that was added to the call stack is the first one to be removed. This is why the function calls are returned in the reverse order of the function calls.

When we first call `sum_up_to(5)`, it is added to the call stack. Then, `sum_up_to(4)` is added to the call stack and so on...

<img src="../../assets/images/recursion-stack-1.png" width="500" />

Once `sumUpTo(1)` is called, it returns 1 and is removed from the call stack. Then, `sumUpTo(2)` returns 3 and is removed from the call stack. This continues until `sumUpTo(5)` returns 15 and is removed from the call stack.

<img src="../../assets/images/recursion-stack-2.png" width="500" />

We can see this by logging the function calls and the return values:

```python
def sum_up_to(n):

    if(n == 1):
        print(f"sum_up_to({n}) returns 1")
        return 1
    
    print(f"sum_up_to({n}) returns sum_up_to({n})" + "{n}")
    result = n + sum_up_to(n-1)
    print(f"sum_up_to({n}) returns {result}")
    return result
```
