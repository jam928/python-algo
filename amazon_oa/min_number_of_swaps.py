def min_number_of_swaps(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    n = len(arr)
    min_number = min(arr)
    max_number = max(arr)

    swap_count = 0
    if (arr[0] == min_number) and (arr[-1] == max_number):
        return swap_count

    for i in range(len(arr)):
        already_sorted = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap & increment count
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap_count += 1

                if arr[0] == min_number and arr[n - 1] == max_number:
                    return swap_count

                already_sorted = False

        if already_sorted:
            break

    return swap_count

print(min_number_of_swaps([9,10,1,3,2]))