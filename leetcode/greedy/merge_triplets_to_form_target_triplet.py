from typing import List


# T: O(N)
# S: O(1)

# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/


def merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
    def can_merge(i):
        for triplet in triplets:
            neighbor_1 = (i + 1) % 3
            neighbor_2 = (i + 2) % 3

            # if the triplet at i is the same as target i
            # and its neighbors are less than or equal to
            # then its guaranteed a triplet at i will equal to target at i
            if triplet[i] == target[i] and triplet[neighbor_1] <= target[neighbor_1] and triplet[neighbor_2] <= target[
                neighbor_2]:
                return True

        return False

    # validate that each triplet can merge to the target triplet
    return can_merge(0) and can_merge(1) and can_merge(2)


print(merge_triplets(triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5]], target=[2, 7, 5]))  # True
print(merge_triplets(triplets=[[3, 4, 5], [4, 5, 6]], target=[3, 2, 5]))  # false
print(merge_triplets(triplets=[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target=[5, 5, 5]))  # true
