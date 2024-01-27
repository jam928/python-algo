# https://leetcode.com/problems/valid-anagram/
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Store the freqs of the chars of s & t in seperate maps
    s_map = {}

    for c in s:
        s_map.update({c: s_map.get(c, 0) + 1})

    t_map = {}

    for c in t:
        t_map.update({c: t_map.get(c, 0) + 1})

    # If the length of both of the freq map do not equal to each other return false
    if len(s_map) != len(t_map):
        return False

    for key, value in s_map.items():
        # if the current element is not in other map or the freq of the key in other map does not equal the current value return false
        if key not in t_map or t_map[key] != value:
            return False

    return True


def is_anagram_2(s: str, t: str) -> bool:
    m = len(s)
    n = len(t)

    if m != n:
        return False

    arr = [0] * 128

    for i in range(m):
        arr[ord(s[i]) - ord('a')] += 1

    for j in range(n):
        arr[ord(t[j]) - ord('a')] -= 1

    # check if the array has reached equilibrium
    for num in arr:
        if num != 0:
            return False

    return True
