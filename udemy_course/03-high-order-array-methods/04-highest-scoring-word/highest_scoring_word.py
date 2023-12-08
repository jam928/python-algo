def highest_scoring_word(s: str) -> str:
    # Split the sentence by space
    words = s.split(' ')

    # map the array of words to an array of scores
    scores = [sum(ord(letter) - ord('a') + 1 for letter in word) for word in words]

    highest_score = max(scores)
    highest_index = scores.index(highest_score)

    return words[highest_index]