# Sets

Now we are going to move on to `sets`. A set is a collection of unique values. A set can contain any data type. You can loop through a set in insertion order. Insertion order is the order in which the values were added to the set. A set is similar to an array, but a set is not indexed and does not contain duplicate values.

## Creating a Set

To create a set, we use the `new` keyword and the `Set()` constructor. Let's create a set called `nameSet`:

```python
nameset = set()
```

We can also pass an array to the `set()` constructor. The values in the array will be added to the set. We can create a set with some values like this:

```python
name_set = set(['John', 'Jane', 'Joe'])
```

Let's log the set:

```python
print(name_set) # { 'John', 'Jane', 'Joe' }
```

We can see that the set has three values. Let's create a set with some duplicate values:

```python
name_set = set(['John', 'Jane', 'Joe', 'Jane', 'Joe'])
```

Let's log the set:

```python
print(name_set) # Set { 'John', 'Jane', 'Joe' }
```

We can see that even though we added duplicate values to the set, the set does not contain any duplicate values. The set only contains unique values, which can be very useful.

## Adding Data

To add data to a set, we use the `add()` method. Let's add some values to the `name_set` set:

```js
name_set.add('Jack')
name_set.add('Jill')
```

Let's log the set:

```js
print(name_set); // Set { 'John', 'Jane', 'Joe', 'Jack', 'Jill' }
```

## Check for a Value

To check for a value in a set, just use `if element in set`:

```python
if 'Jack' in name_set:
    print("Jack is in nameset")
```

## Deleting Data

To delete data from a set, we use the `remove()` method. Let's delete the value `'Jack'` from the set:

```python
name_set.remove('Jack')
```

Let's log the set:

```python
print(name_set) # Set { 'John', 'Jane', 'Joe', 'Jill' }
```

## Getting the Size of a Set

To get the size of a set, we use the `len` property. Let's log the size of the `nameSet` set:

```python
print(len(name_set)) # 4
```

## Looping Through a Set

To loop through a set, we can use the `for...of` loop. Let's loop through the `nameSet` set and log each value:

```python
for e in name_set: 
  print(e)
```

## Converting a Set to an Array

To convert a set to an array, we use the `list` method. Let's convert the `nameSet` set to an array:

```python
name_array = list(name_set)
print(name_array) # [ 'John', 'Jane', 'Joe', 'Jill' ]
```

## Converting an Array to a Set

To convert an array to a set, we use the `Set()` constructor. Let's convert the `nameArray` array to a set:

```python
name_set = set(name_array);
print(name_set) # Set { 'John', 'Jane', 'Joe', 'Jill' }
```

## Deleting All Data from a Set

To delete all data from a set, we use the `clear()` method. Let's delete all data from the `nameSet` set:

```python
name_set.clear();
```

Let's try some challenges using sets.
