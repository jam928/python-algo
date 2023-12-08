# Solution 1
def highest_scoring_word(s: str) -> str:
    # Split the sentence by space
    words = s.split(' ')

    # map the array of words to an array of scores
    scores = [sum(ord(letter) - ord('a') + 1 for letter in word) for word in words]

    highest_score = max(scores)
    highest_index = scores.index(highest_score)

    return words[highest_index]


# Solution 2
def highest_scoring_word_2(s):
    # Split the string into an array of words
    words = s.split()

    # Map the array of words to an array of scores
    scores = [sum(ord(letter) - ord('a') + 1 for letter in word) for word in words]

    # Initialize the highest score and index to 0
    highest_score = 0
    highest_index = 0

    # Loop through the scores array
    for i in range(len(scores)):
        # If the current score is higher than the highest score, update the highest score and index
        if scores[i] > highest_score:
            highest_score = scores[i]
            highest_index = i

    # Return the word with the highest score
    return words[highest_index]