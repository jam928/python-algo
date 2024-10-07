def min_space(s, k):
    s = optimize_str(s)
    last_known_map = {}
    # convert to list
    arr = [c for c in s]

    for i in range(len(arr)):
        if arr[i] not in last_known_map:
            last_known_map[arr[i]] = i
            continue

        space = i - last_known_map[arr[i]]
        if space <= k:
            arr.insert(i, "_")

        last_known_map[arr[i]] = i

    return len(arr)

def optimize_str(s):
    freq_map = {}

    for c in s:
        freq_map[c] = freq_map.get(c, 0) + 1

    # sort by descending order via the values in map
    sorted_by_values = dict(sorted(freq_map.items(), key=lambda kv: kv[1], reverse=True))

    s = ""
    while len(list(sorted_by_values.items())) > 0:
        for k, v in list(sorted_by_values.items()):
            s += k
            sorted_by_values[k] -= 1
            if sorted_by_values[k] == 0:
                del sorted_by_values[k]

    return s


if __name__ == '__main__':
    s1 = "abcabc"
    k1 = 2
    print(min_space(s1,k1))  # 6

    s2 = "abcabc"
    k2 = 3
    print(min_space(s2, k2))  # 7

    s3 = "aaaabbcc"

    k3 = 2
    print(min_space(s3, k3))  # 6