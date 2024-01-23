name_map = {
    1: 'John',
    2: 'Jane',
    3: 'Joe',
}

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

# Getting values
print(name_map.get(1))
print(map_2.get(my_function))
# print(map_2.get(empty_obj))

# Setting values
name_map[4] = 'Jack'
name_map[5] = 'Jill'

# Checking values
print(1 in name_map)
print(6 in name_map)

# Deleting values
name_map.pop(1, None)
print(1 in name_map)

# Get Size
print(len(name_map))

# Iterating (for...in)
for key, value in name_map.items():
    print(key, value)

# Using forEach
for key, value in name_map.items():
    print(key, value)

# Looping keys and values
print(list(name_map.keys()))
print(list(name_map.values()))

# Clearing
name_map.clear()
print(len(name_map))

# print(name_map)
