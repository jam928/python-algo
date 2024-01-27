
# https://leetcode.com/problems/length-of-last-word/description/

def length_of_last_word(s: str) -> int:
    words = s.split()

    length_of_last_word = words[len(words) - 1]

    return len(length_of_last_word)

print(length_of_last_word("Hello World")) # 5
print(length_of_last_word("   fly me   to   the moon  ")) # 4
print(length_of_last_word("luffy is still joyboy")) # 6