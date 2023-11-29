def count_vowels(s):
    vowel_str = "aeiouAEIOU"
    s = s.lower()
    vowel_count = 0
    for c in s:
        if c in vowel_str:
            vowel_count = vowel_count + 1

    return vowel_count


def count_vowels_2(s):
    vowel_str = "aeiouAEIOU"
    return sum(1 for c in s if c in vowel_str)
