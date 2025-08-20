from typing import List

# https://leetcode.com/problems/candy
# T: O(N)
# S: O(N)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        candy = [1 for _ in range(len(ratings))]

        # left -> right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        # right -> left
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1) # max because a child may already have candies from the first pass
        
        total_candies = sum(candy)

        return total_candies
    
if __name__ == '__main__':
    s = Solution()
    assert s.candy(ratings = [1,0,2]) == 5
    assert s.candy(ratings = [1,2,2]) == 4
    assert s.candy(ratings = [1,3,2,2,1]) == 7
    assert s.candy(ratings = [1,2,87,87,87,2,1]) == 13

