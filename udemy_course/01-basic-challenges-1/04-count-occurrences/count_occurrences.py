def count(word, letter):
    letter_count = 0

    for c in word:
        if c == letter:
            letter_count += 1

    return letter_count
