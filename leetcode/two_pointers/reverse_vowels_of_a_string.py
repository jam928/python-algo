
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# T: O(N)
# S: O(N)
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        char_arr = list(s)

        while i < j:
            if s[j] in "AEIOU" or s[j] in "aeiou":
                while (s[i] not in "AEIOU" and s[i] not in "aeiou") and i < j:
                    i += 1
                temp = char_arr[i]
                char_arr[i] = char_arr[j]
                char_arr[j] = temp
                i+=1
            
            j-=1
        
        return ''.join(char_arr)
    
if __name__ == '__main__':
    s = Solution()
    assert s.reverseVowels("IceCreAm") == "AceCreIm"
    assert s.reverseVowels("leetcode") == "leotcede"