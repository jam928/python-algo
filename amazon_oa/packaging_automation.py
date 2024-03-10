def packaging(numGroups, arr):
    """
    :type numGroups: int
    :type arr: List[int]
    :rtype: int
    """

    # sort the array
    arr.sort()

    # update array elements in place if its left neighbor diff is greater than 1
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            arr[i] = arr[i - 1] + 1

    return arr[len(arr) - 1]

print(packaging(4, [3,1,3,4]))
print(packaging(4, [1,3,2,2]))
print(packaging(4, [1,1,1,1]))
print(packaging(4, [3,2,3,5]))