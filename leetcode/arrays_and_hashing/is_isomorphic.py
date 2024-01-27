# https://leetcode.com/problems/isomorphic-strings/

def is_isomorphic(s: str, t: str) -> bool:
    s_to_t_map = {}
    t_to_s_map = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t_map and s_to_t_map[char_s] != char_t:
            return False
        s_to_t_map[char_s] = char_t

        if char_t in t_to_s_map and t_to_s_map[char_t] != char_s:
            return False
        t_to_s_map[char_t] = char_s

    return True

print(is_isomorphic("egg", "add"))      # Output: True
print(is_isomorphic("foo", "bar"))      # Output: False
print(is_isomorphic("paper", "title"))  # Output: True