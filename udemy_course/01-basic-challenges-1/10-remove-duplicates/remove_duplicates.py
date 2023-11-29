def remove_duplicates(arr):
    unique_arr = []

    s = set()
    boolean_set = set()

    for e in arr:
        if isinstance(e, bool) and e not in boolean_set:
            boolean_set.add(e)
            unique_arr.append(e)
        elif not isinstance(e, bool) and e not in s:
            unique_arr.append(e)
            s.add(e)

    return unique_arr
