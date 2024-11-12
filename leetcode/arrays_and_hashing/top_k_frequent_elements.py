from collections import defaultdict, Counter
from typing import List


# https://leetcode.com/problems/top-k-frequent-elements/

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq_map = Counter(nums)
    freq = [[] for _ in range(len(nums) + 1)] # count as index, list of associated values for that particular index

    for num, count in freq_map.items():
        freq[count].append(num)

    result = []
    for i in range(len(freq) - 1, -1, -1):
        if len(freq[i]) == 0:
            continue
        if len(result) == k:
            break
        result.extend(freq[i])

    return result

print(top_k_frequent([1,1,1,2,2,3], 2)) # [1,2]
print(top_k_frequent([1], 1)) # [1]