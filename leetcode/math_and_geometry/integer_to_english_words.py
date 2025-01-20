
# https://leetcode.com/problems/integer-to-english-words/description/
# T: O(1)
# S: O(1)

class Solution:

    def __init__(self):
        self.big_string = ["Thousand", "Million", "Billion"]
        self.digit_string = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.teen_string = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                            "Eighteen", "Nineteen"]
        self.ten_string = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        result = self.helper(num % 1000)
        num //= 1000

        for i in range(len(self.big_string)):
            if num > 0 and num % 1000 > 0:
                result = self.helper(num % 1000) + self.big_string[i] + " " + result
            num //= 1000

        return result.strip()

    def helper(self, num) -> str:
        result = ""

        if num > 99:
            result += self.digit_string[num // 100] + " Hundred "

        num %= 100
        if num < 20 and num > 9:
            result += self.teen_string[num - 10] + " "
        else:
            if num >= 20:
                result += self.ten_string[num // 10] + " "
            num %= 10
            if num > 0:
                result += self.digit_string[num] + " "

        return result

if __name__ == "__main__":
    print(Solution().numberToWords(123)) # One Hundred Twenty Three
    print(Solution().numberToWords(12345)) # Twelve Thousand Three Hundred Forty Five
    print(Solution().numberToWords(1234567)) # One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven