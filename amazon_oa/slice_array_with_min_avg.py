def slice_array_with_min_average(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    # get total sum of the array
    total_sum = sum(arr)

    min_diff = float('inf')

    result = 0
    current_sum = 0
    for i in range(len(arr) - 1):
        current_sum += arr[i]
        current_avg = current_sum / (i + 1)

        total_sum -= arr[i]
        total_avg = total_sum / (len(arr) - (i + 1))

        # to store the minimum diff
        diff = current_avg - total_avg

        # update min_diff
        if diff < min_diff and diff > 0:
            min_diff = diff
            result = i + 1

    return result
print(slice_array_with_min_average([1,3,5,2,1]))
print(slice_array_with_min_average([1,1.1,-2]))
