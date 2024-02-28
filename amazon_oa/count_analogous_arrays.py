def count_analogous_arrays_bf(A, lower_bound, upper_bound):
    a = set(range(lower_bound, upper_bound + 1))
    b = set()

    for diff in A:
        for num in a:
            if lower_bound <= num + diff <= upper_bound:
                b.add(num + diff)

        a = b
        b = set()

    return len(a)


def count_analogous_arrays(A, lower_bound, upper_bound):
    mi = 0
    mx = 0
    total_sum = 0

    for num in A:
        total_sum += num
        mi = min(mi, total_sum)
        mx = max(mx, total_sum)

    return max(0, upper_bound - lower_bound - (mx - mi) + 1)


# Example usage:
# A = [-2, -1, -2, 5]
# lower_bound = 3
# upper_bound = 10
# print(count_analogous_arrays_bf(A, lower_bound, upper_bound))
# print(count_analogous_arrays(A, lower_bound, upper_bound))

arr = [-2,-1,-2,5]
lower_bound = 3
upper_bound = 10
print(count_analogous_arrays(arr, lower_bound, upper_bound)) # 3

arr = [1, 0, 3, 0]
lower_bound = 0
upper_bound = 4
print(count_analogous_arrays(arr, lower_bound, upper_bound)) # 1

arr = [1, 1, 3, 2]
lower_bound = 1
upper_bound = 5
print(count_analogous_arrays(arr, lower_bound, upper_bound)) # 2