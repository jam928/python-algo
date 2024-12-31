from collections import Counter
from heapq import heappop, heappush

# https://leetcode.com/problems/reorganize-string/

# T: O(nlogn)
# S: O(n)

class Pair:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq  # higher freq gets higher priority


def reorganize_string(s: str) -> str:
    # count the freq of each character
    freq_map = Counter(s)

    # create max heap
    pq = []

    for char, freq in freq_map.items():
        heappush(pq, Pair(char, freq))

    result = []
    prev = heappop(pq)
    result.append(prev.char)
    prev.freq -= 1

    while pq:
        # pop the next most freq element
        current = heappop(pq)
        result.append(current.char)
        current.freq -= 1

        # if the previous element still has a freq
        # push it back into the heap
        if prev.freq > 0:
            heappush(pq, prev)

        # update prev to the current element
        prev = current

    return ''.join(result) if len(result) == len(s) else ""

if __name__ == '__main__':
    s = "aab"
    print(reorganize_string(s)) # aba

    s = "aaab"
    print(reorganize_string(s)) # ""