def array_intersection(arr1, arr2):
    intersection = []

    for element in arr1:
        if element in arr2 and element not in intersection:
            intersection.append(element)

    return intersection

def array_intersection_2(arr1, arr2):
    s = set()

    for e in arr1:
        s.add(e)

    intersection_arr = []

    for e in arr2:
        if e in s:
            intersection_arr.append(e)

    return intersection_arr

def array_union(arr1, arr2):
    union_set = set(arr1).union(arr2)
    union_arr = list(union_set)
    return union_arr