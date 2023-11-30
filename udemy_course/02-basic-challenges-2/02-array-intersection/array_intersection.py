def array_intersection(arr1, arr2):
    s = set()

    for e in arr1:
        s.add(e)

    intersection_arr = []

    for e in arr2:
        if e in s:
            intersection_arr.append(e)

    return intersection_arr