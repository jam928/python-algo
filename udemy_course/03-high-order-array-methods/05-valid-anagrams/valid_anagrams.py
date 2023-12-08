def valid_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    freq_count_map = {}

    for c in str1:
        freq_count_map.update({c: freq_count_map.get(c, 0) + 1})

    for c in str2:
        if c not in freq_count_map:
            return False
        freq_count_map.update({c: freq_count_map.get(c) - 1})

        if freq_count_map.get(c) == 0:
            freq_count_map.pop(c)

    return len(freq_count_map) == 0
