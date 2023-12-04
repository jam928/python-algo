def find_first_non_repeating_character(s):
    freq_count_map = {}

    for c in s:
        freq_count_map.update({c: freq_count_map.get(c, 0) + 1})

    for c in s:
        if freq_count_map.get(c) == 1:
            return c

    return None