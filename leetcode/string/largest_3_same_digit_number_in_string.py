# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
# T: O(N)
# S: O(1)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ["", -1]

        for i in range(0, len(num)-2):
            if int(num[i]) == int(num[i+1]) and int(num[i+1]) == int(num[i+2]) and int(num[i:i+3]) > largest[1]:
                largest[0] = num[i:i+3]
                largest[1] = int(num[i:i+3])

        return largest[0]

if __name__ == '__main__':
    s = Solution()
    assert s.largestGoodInteger("6777133339") == "777"
    assert s.largestGoodInteger("2300019") == "000"
    assert s.largestGoodInteger("42352338") == ""