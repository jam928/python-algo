def max_subarray_sum(arr, k):
    current_sum = 0
    max_sum = 0

    for i in range(k):
        max_sum += arr[i]

    current_sum = max_sum

    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(current_sum, max_sum)

    return max_sum