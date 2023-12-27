import timeit


def access_element(arr, index):
    return arr[index]


arr1 = [1, 2, 3, 4, 5]
time1 = timeit.timeit(lambda: access_element(arr1, 1), number=100000)
print("Access Element 1:", time1)

arr2 = list(range(1, 10001))
time2 = timeit.timeit(lambda: access_element(arr2, 1), number=100000)
print("Access Element 2:", time2)
