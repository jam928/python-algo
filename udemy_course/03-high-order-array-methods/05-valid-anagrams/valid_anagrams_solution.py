def valid_anagrams(str1, str2):
    # Initialize dictionaries for character frequencies
    freq_count1 = {}
    freq_count2 = {}

    freq_count1 = {char: freq_count1.get(char, 0) + 1 for char in str1}

    freq_count2 = {char: freq_count2.get(char, 0) + 1 for char in str2}

    # Compare the two dictionaries of character frequencies
    return all(freq_count1[char] == freq_count2[char] for char in freq_count1)
