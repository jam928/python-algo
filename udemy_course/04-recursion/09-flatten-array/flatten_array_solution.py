def flatten_array(arr):
    # Create an empty list to store the result
    result = []

    # Loop through each item in arr
    for item in arr:
        # If item is a list, call flatten_array again and extend the result to result
        if isinstance(item, list):
            result.extend(flatten_array(item))
        else:
            # If item is not a list, append it to result
            result.append(item)

    return result

result = flatten_array([1, 2, 3, [4, 5, [6, 7, 8], 9], 10])

print(result)