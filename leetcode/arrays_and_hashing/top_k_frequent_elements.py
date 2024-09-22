from collections import defaultdict
from typing import List


# https://leetcode.com/problems/top-k-frequent-elements/

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # store the freq of each element in a map
    freq_map = defaultdict(int)

    for num in nums:
        freq_map[num] += 1

    # sort the freq map values by greatest to least
    sorted_items_by_value = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

    result = []

    for i in range(0, k):
        result.append(sorted_items_by_value[i][0])

    return result

print(top_k_frequent([1,1,1,2,2,3], 2)) # [1,2]
print(top_k_frequent([1], 1)) # [1]