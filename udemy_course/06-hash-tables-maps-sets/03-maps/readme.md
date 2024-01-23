# Maps

## Maps vs Objects

Maps are similar to objects in that both let you set keys to values, retrieve those values, delete keys, and detect whether something is stored at a key. Objects are used more because they have been around longer, but maps are preferred in certain cases. The biggest difference between maps and objects is that maps allow keys of any type, while objects only allow strings, numbers, and symbols as keys. This means that maps can use functions, objects, and any primitive type as a key.

Maps can also have better performance in scenarios involving frequent additions and removals of key-value pairs. On the other hand, objects have better performance for the case of looking up key-value pairs.

## Creating a Map

To create a map, we use the `{}`

```python
name_map = {}
```

Initialize a map with values

```python
name_map = {
    1: 'John',
    2: 'Jane',
    3: 'Joe',
}

```

Let's log the map:

```python
print(name_map)
```

We can see that the map has three key-value pairs. The keys are the numbers 1, 2, and 3, and the values are the strings 'John', 'Jane', and 'Joe'. Notice that I used numbers as keys in this example. We can use any type of data as a key, including objects and functions. Let's create a map with some different types of keys:

```python
my_function = lambda: None
empty_obj = {}

map_2 = {
    'name': 'John',
    1: 'number one',
    True: 'really true',
    None: 'null',
    my_function: 'empty function',
    frozenset(empty_obj.items()): 'empty object',
}
```

## Retrieving Data

To retrieve data from a map, we use the `get()` method. Let's retrieve the value associated with the key `1` from the `nameMap` map:

```python
print(name_map.get(1)) # John
```

Let's get the function and the object values from the `map2` map:

```python
print(map_2.get(my_function))
# print(map_2.get(empty_obj))
```

## Setting Data

To set data in a map, just <name_of_map>[`key`] = 'New Value'

```python
# Setting values
name_map[4] = 'Jack'
name_map[5] = 'Jill'
```

Let's log the map:

```python
print(name_map); # Map(5) { 1 => 'John', 2 => 'Jane', 3 => 'Joe', 4 => 'Jack', 5 => 'Jill' }
```

## Checking if a Key Exists

To check if a key exists in a map, we use the `in` keyword. Let's check if the key `1` exists in the `name_map` map:

``` python
# Checking values
print(1 in name_map) # True
print(6 in name_map) # False

```

## Deleting Data

To delete data from a map, we use the `pop()` method. Let's delete the key-value pair with the key `1` from the `nameMap` map:

```python
# Deleting values
name_map.pop(1, None)
print(1 in name_map)
```

## Getting the Size of a Map

To get the size of a map, we use the `len` property. Let's log the size of the `name_map` map:

```python
# Get Size
print(len(name_map))
```

## Iterating Through a Map

To iterate/loop through a map, we can use the `for...of` loop. Let's loop through the `name_map` map and log each key-value pair:

```python
for key, value in name_map.items():
    print(key, value)
```

You can also get all of the keys or values from a map using the `keys()` and `values()` methods. Let's log all of the keys and values from the `name_map` map:

```python
# Looping keys and values
print(list(name_map.keys()))
print(list(name_map.values()))
```

## Clearing a Map

To clear a map, we use the `clear()` method. Let's clear the `name_map` map:

```python
# Clearing
name_map.clear()
print(len(name_map))
```

Now let's try some challenges!
