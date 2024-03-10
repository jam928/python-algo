def append_characters(s: str, t: str) -> int:
    # init pointers for s and t
    s_ptr = t_ptr = 0

    # iterate through both strings
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
            t_ptr += 1
        else:
            # increment the s_ptr till we reach the above again
            s_ptr += 1

    return len(t) - t_ptr


print(append_characters("coaching", "coding"))  # 4
print(append_characters("abcde", "a"))  # 0
print(append_characters("z", "abcde"))  # 5
