# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
from collections import defaultdict
from typing import List


def interchangeable_rectangles(rectangles: List[List[int]]) -> int:
    freq_map = defaultdict(int)  # w/h: count

    for w, h in rectangles:
        freq_map[w / h] += 1

    result = 0
    # use combinations formula: (n * (n-1)) / 2
    for c in freq_map.values():
        if c <= 1:
            continue
        result += (c * (c - 1)) // 2

    return result

if __name__ == '__main__':
    print(interchangeable_rectangles([[4,8],[3,6],[10,20],[15,30]])) # 6
    print(interchangeable_rectangles([[4,5], [7,8]])) # 0