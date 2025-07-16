from collections import deque

# https://leetcode.com/problems/add-strings/

# T: O(max(M,N))
# S: O(max(M,N))

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # iterate from right to left
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = deque()
        while i >= 0 or j >= 0 or carry > 0:
            first_num = int(num1[i]) if i >= 0 else 0
            second_num = int(num2[j]) if j >= 0 else 0

            current_sum = first_num + second_num + carry
            result.appendleft(str(current_sum % 10))

            carry = current_sum // 10

            i -= 1
            j -= 1

        return ''.join(result)

if __name__ == '__main__':
    s = Solution()

    num1 = "11"
    num2 = "123"
    result = s.addStrings(num1, num2)
    print(result) # 134

    num1 = "456"
    num2 = "77"
    result = s.addStrings(num1, num2)
    print(result)  # 533

    num1 = "0"
    num2 = "0"
    result = s.addStrings(num1, num2)
    print(result) # 0