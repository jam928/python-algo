def range_of_numbers(start_num, end_num):
    # Check if the start_num is equal to end_num (base case)
    if start_num == end_num:
        # If they are equal, return a list containing just the start_num
        return [start_num]

    # If they are not equal, call the range_of_numbers function recursively on a smaller range
    # This creates a list of numbers from start_num to end_num - 1
    numbers = range_of_numbers(start_num, end_num - 1)

    # Append the current value of end_num to the 'numbers' list
    numbers.append(end_num)

    # Return the 'numbers' list containing all the numbers from start_num to end_num
    return numbers


# Example usage:
result = range_of_numbers(1, 5)
print(result)  # Output: [1, 2, 3, 4, 5]
