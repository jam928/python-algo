from collections import defaultdict
from typing import List

# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

def find_matrix(nums: List[int]) -> List[List[int]]:
    # get freq map of elements
    freq_map = defaultdict(int)

    for num in nums:
        freq_map[num] += 1

    # sort freq map by val in desc order
    sorted_freq_map = dict(sorted(freq_map.items(), key=lambda kv: kv[1], reverse=True))

    result = []

    # add each result to list
    while len(sorted_freq_map) >= 1:
        arr = []
        for k in list(sorted_freq_map.keys()):
            arr.append(k)
            sorted_freq_map[k] -= 1
            if sorted_freq_map[k] == 0:
                del sorted_freq_map[k]
        result.append(arr)

    return result

if __name__ == '__main__':
    print(find_matrix([1,3,4,1,2,3,1]))