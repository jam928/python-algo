# https://leetcode.com/problems/multiply-strings/
# T: O(m * n)
# S: O(m * n)

def multiply(num1: str, num2: str) -> str:
    # return zero if any of the strings equal zero
    if "0" == num1 or "0" == num2:
        return "0"

    dp = [0] * (len(num1) + len(num2))
    dp_index = len(dp) - 1

    for i in range(len(num1) - 1, -1, -1):
        index = dp_index
        for j in range(len(num2) - 1, -1, -1):
            result = int(num1[i]) * int(num2[j]) + dp[index]
            dp[index] = result % 10  # just get the remainder for that particular index
            dp[index - 1] += result // 10  # add to carry for the index on its left
            index -= 1

        dp_index -= 1

    result = ''.join(map(str, dp)).lstrip('0')

    return result if result else '0'


print(multiply("2", "3"))  # 6
print(multiply("123", "456"))  # 56088
print(multiply("408", "5"))  # 2040
