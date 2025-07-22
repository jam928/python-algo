from typing import List

# https://leetcode.com/problems/subsets/
# T: O(2^N)
# S: O(2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def subsets_helper(sub_list, start):
            # append sublist
            result.append(list(sub_list))

            for i in range(start, len(nums)):
                # append current number
                sub_list.append(nums[i])
                subsets_helper(sub_list, i + 1)
                # remove element when backtracking
                sub_list.pop()

        subsets_helper([], 0)

        return result

if __name__ == '__main__':
    s = Solution()
    assert s.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert s.subsets([0]) == [[],[0]]