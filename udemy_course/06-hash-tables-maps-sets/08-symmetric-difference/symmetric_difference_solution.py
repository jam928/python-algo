def symmetric_difference(arr1, arr2):
    # Create a set from arr1 and arr2
    set1 = set(arr1)
    set2 = set(arr2)
    # Create a result list
    result = []

    # Iterate through arr1 and check if the current number is not in set2
    for num in arr1:
        if num not in set2:
            # If it is not in set2, append it to the result list
            result.append(num)

    # Iterate through arr2 and check if the current number is not in set1
    for num in arr2:
        # If it is not in set1, append it to the result list
        if num not in set1:
            result.append(num)

    # Return the result list
    return result
