def max_subarray_quadratic(arr, k):
    max_sum = 0

    for i in range(len(arr) - k):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]

        max_sum = max(current_sum, max_sum)

    return max_sum
