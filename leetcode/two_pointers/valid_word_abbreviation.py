# T: O(M)
# S: O(1)

# https://leetcode.com/problems/valid-word-abbreviation/description/
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            # get the number in abbr if its a number
            if abbr[j].isdigit():
                if abbr[j] == '0':  # zero leading case
                    return False

                num = []
                while j < len(abbr) and abbr[j].isdigit():
                    num.append(abbr[j])
                    j += 1

                i += int(''.join(num))
            else:
                if i >= len(word) or word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

        return i == len(word) and j == len(abbr)

if __name__ == '__main__':

    s = Solution()
    word = "internationalization"
    abrr = "i12iz4n"
    print(s.validWordAbbreviation(word, abrr)) # true

    word = "apple"
    abrr = "a2e"
    print(s.validWordAbbreviation(word, abrr))  # false