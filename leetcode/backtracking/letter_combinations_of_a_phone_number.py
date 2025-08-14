from typing import List


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# T: O(N * (4 ^ N))
# S: O(N * (4 ^ N))

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        # store digit along with its letter combination in a map
        phone_button_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        # use a helper function to return all possible combinations
        def helper(current_list, index):
            # base case: if the current list length is the same as digits length add it to result list
            if len(current_list) == len(digits) and len(current_list) != 0:
                result.append(''.join(current_list))
                return

            # recursively attempt all possible combinations
            for i in range(index, len(digits)):
                letters = phone_button_mapping[digits[i]]
                for j in range(0, len(letters)):
                    current_list.append(letters[j])
                    helper(current_list, i + 1)
                    current_list.pop()

        helper([], 0)
        return result

if __name__ == '__main__':
    s = Solution()
    assert s.letterCombinations("23") ==  ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert s.letterCombinations("") == []
