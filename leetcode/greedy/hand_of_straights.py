from collections import defaultdict
from typing import List

# https://leetcode.com/problems/hand-of-straights/description/
# T: O(nlogn)
# S: O(n)

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False

    freq_map = defaultdict(int)

    for h in hand:
        freq_map[h] += 1

    for key in sorted(freq_map.keys()):
        value = freq_map[key]

        if value <= 0:
            continue

        for i in range(groupSize):
            if freq_map.get(key + i, 0) < value:
                return False
            freq_map[key + i] -= value

    return True

print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3)) # true
print(isNStraightHand(hand = [1,2,3,4,5], groupSize = 4)) # false