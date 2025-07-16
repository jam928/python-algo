from collections import defaultdict
from typing import List

# https://leetcode.com/problems/fruit-into-baskets/
# T: O(N)
# S: O(N)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        fruit_map = defaultdict(int)

        i = 0

        max_fruits = 0

        for j in range(len(fruits)):
            fruit_map[fruits[j]] += 1

            if len(fruit_map) > k and i < len(fruits):
                fruit_map[fruits[i]] -= 1
                if fruit_map[fruits[i]] == 0:
                    del fruit_map[fruits[i]]
                i += 1

            max_fruits = max(max_fruits, j - i + 1)

        return max_fruits

if __name__ == '__main__':
    solution = Solution()
    fruits = [1,2,1]
    result = solution.totalFruit(fruits)
    print(result) # 3

    fruits = [0,1,2,2]
    result = solution.totalFruit(fruits) # 3
    print(result)  # 3

    fruits = [1,2,3,2,2]
    result = solution.totalFruit(fruits)  # 4
    print(result)  # 3



