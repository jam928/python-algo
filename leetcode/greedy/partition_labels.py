from typing import List


# T: O(n)
# S: O(1)
# https://leetcode.com/problems/partition-labels/description/


def partition_labels(s: str) -> List[int]:
    # store last indexes in a map
    last_index = {}

    for i in range(len(s)):
        c = s[i]
        last_index[c] = i

    result = []

    size = 0
    last_known_index = 0

    for i in range(len(s)):
        size += 1

        last_known_index = max(last_known_index, last_index[s[i]])

        # once we reached i from the last recorded index
        # then we know we partition from the size recorded
        if i == last_known_index:
            # add size to list and reset it to the next partition
            result.append(size)
            size = 0

    return result


print(partition_labels("ababcbacadefegdehijhklij"))  # [9,7,8]
print(partition_labels("eccbbbbdec"))  # [10]
