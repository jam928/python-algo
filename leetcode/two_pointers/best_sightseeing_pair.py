from typing import List

# T: O(N)
# S: O(1)
# https://leetcode.com/problems/best-sightseeing-pair/description/

def max_score_sight_seeing_pair(values: List[int]) -> int:
    # values[i] + values[j] + i - j -> (values[i] + i) + (values[j] - j)
    max_score = float('-inf')
    first_spot = values[0]

    for j in range(1, len(values)):
        if values[j] - j + first_spot > max_score:
            max_score = values[j] - j + first_spot

        if values[j] + j > first_spot:
            first_spot = values[j] + j

    return max_score

if __name__ == '__main__':
    print(max_score_sight_seeing_pair([8,1,5,2,6])) # 11
    print(max_score_sight_seeing_pair([1,2])) # 2
