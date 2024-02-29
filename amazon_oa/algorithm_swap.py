def how_many_swaps(arr):
    n = len(arr)

    swap_count = 0

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap & increment swap count
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap_count += 1

                # since you already swapped mark the already sorted flag as false
                already_sorted = False

        # break out if flag is true
        if already_sorted:
            break
    return swap_count


print(f"Swaps: {how_many_swaps([5, 1, 4, 2])}")
