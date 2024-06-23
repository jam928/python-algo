# T: O(n * Σ(P(N, k)))
# S: O(n)
from collections import Counter
from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    permutations = []

    counter = Counter(nums)

    def helper(result):
        if len(result) == len(nums):
            permutations.append(list(result))
            return

        for key in counter:
            if not counter[key]:
                continue
            counter[key] -= 1  # decrement visited key
            helper(result + [key])
            counter[key] += 1  # restore the state of visited key to find the next path

    helper([])
    return permutations

print(permute_unique([1,1,2])) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
# print(permute_unique([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]