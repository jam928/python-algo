from typing import List

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < abs(asteroid):
                    stack.pop()

                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)

        return stack

if __name__ == '__main__':
    s = Solution()
    assert s.asteroidCollision([5,10,-5]) == [5,10]
    assert s.asteroidCollision([8,-8]) == []
    assert s.asteroidCollision([10,2,-5]) == [10]