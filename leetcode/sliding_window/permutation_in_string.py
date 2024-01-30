def check_inclusion(s1: str, s2: str) -> bool:
    freq_count = {}

    for c in s1:
        freq_count[c] = freq_count.get(c, 0) + 1

    i = 0
    matched = 0
    for j in range(len(s2)):

        right = s2[j]

        if right in freq_count:
            freq_count[right] = freq_count.get(right) - 1

            if freq_count[right] == 0:
                matched += 1

        # shrink the window if j is greater than s1 length
        if j >= len(s1) - 1:
            if matched == len(freq_count):
                return True

            left = s2[i]
            if left in freq_count:
                if freq_count[left] == 0:
                    matched -= 1
                freq_count[left] = freq_count.get(left) + 1
            i += 1

    return False

print(check_inclusion(s1 = "ab", s2 = "eidbaooo")) # true
print(check_inclusion(s1 = "ab", s2 = "eidboaoo")) # false
