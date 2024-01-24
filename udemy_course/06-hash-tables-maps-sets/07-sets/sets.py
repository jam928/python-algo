# Create a set (try adding duplicate values)
name_set = set(['John', 'Jane', 'Joe', 'John', 'Joe'])

# Add values to set
name_set.add('Jack')
name_set.add('Jill')

print(name_set)

# Check for values
print('Jill' in name_set)

# Delete from set
name_set.remove('Jill')

print(name_set)

# Get size of set
print(len(name_set))

# Get all values from set
print(name_set)

# Iterate through set
for name in name_set:
    print(name)

# Convert set to list
name_list = list(name_set)
print(name_list)

# Clear set
name_set.clear()