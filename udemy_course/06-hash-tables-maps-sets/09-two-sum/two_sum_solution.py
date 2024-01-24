def two_sum(nums, target):
    # Create a set to store numbers that have been seen
    num_set = set()

    # Iterate through the input list
    for i in range(len(nums)):
        # Calculate the complement needed to reach the target sum
        # nums[i] represents the current number being iterated in the list.
        # target is the desired sum we're trying to achieve with two numbers.
        # target - nums[i] calculates the difference between the target sum and the current number. This value is the complement.
        complement = target - nums[i]

        # If the complement is found in the num_set, return the indices of the two numbers
        if complement in num_set:
            return [nums.index(complement), i]

        # Add the current number to the num_set
        num_set.add(nums[i])

    # If no solution is found, return an empty list
    return []