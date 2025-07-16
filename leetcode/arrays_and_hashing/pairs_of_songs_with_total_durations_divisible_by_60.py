from collections import defaultdict
from typing import List

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
# T: O(N)
# S: O(N)

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = defaultdict(int)

        pairs = 0

        for duration in time:
            hashed_time = duration % 60
            complement = 60 - hashed_time if hashed_time > 0 else 0

            pairs += seen[complement]

            seen[hashed_time] += 1

        return pairs

if __name__ == '__main__':
    time = [30,20,150,100,40]
    s = Solution()
    print(s.numPairsDivisibleBy60(time)) # 3

    time = [60,60,60]
    s = Solution()
    print(s.numPairsDivisibleBy60(time)) # 3