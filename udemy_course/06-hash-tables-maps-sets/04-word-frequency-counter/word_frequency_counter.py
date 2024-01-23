import string
from collections import defaultdict

def remove_punctuation(input_str):
    # Create a translation table to map each punctuation mark to None
    translator = str.maketrans('', '', string.punctuation)

    result_str = input_str.translate(translator)

    return result_str

def word_frequency_counter(s: str):
    # Convert the string to all lowercase; remove the whitespace; remove the punctuation chars
    s = remove_punctuation(s).lower().split()

    freq_count = {}
    for word in s:
        freq_count.update({word: freq_count.get(word, 0) + 1})
    return freq_count