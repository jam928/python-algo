def longest_consecutive_sequence(nums):
    # Create new set
    num_set = set(nums)
    # Create longest sequence variable
    longest_sequence = 0

    # Loop through set
    for num in num_set:
        # If set does not have num - 1, identify the starting element of a potential consecutive sequence.
        if num - 1 not in num_set:
            # Create current num and current sequence variables
            current_num = num
            current_sequence = 1

            # While set has current num + 1, is the next consecutive number in the set?
            while current_num + 1 in num_set:
                # Increment current num and current sequence
                current_num += 1
                current_sequence += 1

            # Set longest sequence to the max of longest sequence and current sequence
            longest_sequence = max(longest_sequence, current_sequence)

    # Return longest sequence
    return longest_sequence