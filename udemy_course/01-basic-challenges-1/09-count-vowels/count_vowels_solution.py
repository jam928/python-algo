def count_vowels(s):
    formattedStr = s.lower()

    vowel_count = 0

    for c in formattedStr:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowel_count = vowel_count + 1

    return vowel_count
