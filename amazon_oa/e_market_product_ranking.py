def get_items(entries):
    """
    :type entries: List[str]
    :rtype: List[str]
    """
    items = []

    k = 0
    result = []
    for entry in entries:
        if entry[0] == 'VIEW':
            items.sort(key=lambda x: (x[0], x[1]))
            result.append(items[k][1])
            k += 1
        if entry[0] != 'INSERT':
            continue
        dollar_amt = int(entry[2])
        items.append((dollar_amt, entry[1]))

    return result
