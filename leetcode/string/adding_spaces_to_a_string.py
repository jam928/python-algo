from typing import List

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/adding-spaces-to-a-string/description/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Use list for easy string manipulation
        result = []

        i = 0  # pointer for spaces array

        for j, c in enumerate(s):
            if i < len(spaces) and j == spaces[i]:
                result.append(' ')
                i += 1
            result.append(c)

        return ''.join(result)

if __name__ == '__main__':
    s = Solution()

    # "Leetcode Helps Me Learn"
    print(s.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))

    # "i code in py thon"
    print(s.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))

    # " s p a c i n g"
    print(s.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))