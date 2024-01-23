import re


def word_frequency_counter(s):
    # Convert the string to lowercase and split it into an array of words
    words = re.findall(r'\w+', s.lower())

    # Create an empty dictionary to store word frequencies
    word_frequency = {}

    # Loop through each word in the array
    for word in words:
        # If the word is already in the dictionary, increment its frequency
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            # If the word is not in the dictionary, add it with a frequency of 1
            word_frequency[word] = 1

    return word_frequency
