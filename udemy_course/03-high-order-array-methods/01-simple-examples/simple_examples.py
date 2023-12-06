import functools

numbers = [1, 2, 3, 4, 5]


#
# map: Executes a specified function for each item in an iterable. The item is sent to the function as a parameter
#

def doubled_numbers(num):
    return num * 2


result = list(map(doubled_numbers, numbers))
print(result)


# Output: [2, 4, 6, 8, 10]


#
# filter: Creates a new array with elements that satisfy a specified condition.
#

def even_numbers(num):
    return num % 2 == 0


result = list(filter(even_numbers, numbers))

print(result)


#
#  reduce: Accumulates array elements into a single value using a provided function.
#
def sum(x, y):
    return x + y


total_sum = functools.reduce(sum, numbers)
print(total_sum)

#
# forEach: Iterates through array elements and applies a function without creating a new array.(use list comprehensions for python)
#

print(' '.join([str(num) for num in numbers]))

#
# next: Returns the first array element that satisfies a specified condition. (use next in python)
#
first_even = next((num for num in numbers if num % 2 == 0), None)
print(first_even)

#
# any: Checks if at least one array element satisfies a condition.
#
has_even = any(num for num in numbers if num % 2 == 0)

print(has_even)

#
# all: Checks if all array elements satisfy a condition.
#

all_even = all(num % 2 == 0 for num in numbers)

print(all_even)