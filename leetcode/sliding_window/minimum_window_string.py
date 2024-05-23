
# T: O(s + t)
# S: O(s + t)
# https://leetcode.com/problems/minimum-window-substring/description/


def min_window(s: str, t: str) -> str:
    # use 2 hashmaps with what we have currently and the t map
    need_map = {}
    window = {}

    for c in t:
        need_map[c] = need_map.get(c, 0) + 1

    need = len(need_map)
    have = 0

    indices = [0, 0]
    min_len = len(s) + 1

    i = 0

    for j in range(0, len(s)):
        right = s[j]

        if right in need_map:
            # update the count in the have of current character
            window[right] = window.get(right, 0) + 1
            if window[right] == need_map[right]:
                have += 1

        # shrink the window if the have and need are equal to each other
        while have == need:

            # update the current min_len if needed
            window_size = j - i + 1
            if window_size < min_len:
                indices = [i, j]
                min_len = window_size

            # decrement the freq count from the left ptr
            left = s[i]
            if left in need_map:
                window[left] = window.get(left) - 1
                if window[left] < need_map[left]:
                    have -= 1
            i += 1

    l = indices[0]
    r = indices[1]

    return "" if min_len > len(s) else s[l:r + 1]


if __name__ == '__main__':
    print(min_window(s="ADOBECODEBANC", t="ABC"))  # "BANC"
    print(min_window(s="a", t="a"))  # "a"
    print(min_window(s="a", t="aa"))  # ""
