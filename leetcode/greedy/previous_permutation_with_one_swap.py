from typing import List

# https://leetcode.com/problems/previous-permutation-with-one-swap/description/
# T: O(N)
# S: O(1)

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i < 0:
            return arr

        j = n - 1

        while arr[j] >= arr[i] or (j > 0 and arr[j] == arr[j - 1]):
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]
        return arr

if __name__ == '__main__':
    s = Solution()
    assert s.prevPermOpt1([3,2,1]) == [3,1,2]
    assert s.prevPermOpt1([1,1,5]) == [1,1,5]
    assert s.prevPermOpt1([1,9,4,6,7]) == [1,7,4,6,9]