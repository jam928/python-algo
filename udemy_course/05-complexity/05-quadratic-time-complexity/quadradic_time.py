#
# Quadradic Time O(n^2)
#
# Quadradic time means that the time required to complete a function is proportional to the square of the input data set.
#
import time


def sum_array(arr):
    sum = 0
    sum2 = 0

    for i in range(len(arr)):
        sum += arr[i]
        for j in range(len(arr)):
            sum2 += arr[j]

    return sum + sum2


arr1 = [1, 2, 3, 4, 5]
start = time.time()
print(sum_array(arr1))
end = time.time()
print(f"Sum array1 took: {end - start} ms")

arr2 = list(range(1, 10000))
start = time.time()
print(sum_array(arr2))
end = time.time()
print(f"Sum array2 took: {end - start} ms")
