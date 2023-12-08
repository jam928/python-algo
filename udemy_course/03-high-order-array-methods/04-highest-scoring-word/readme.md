# Challenge: Highest Scoring Word

## Instructions

Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according to its position in the alphabet: `a` = 1, `b` = 2, `c` = 3, and so on.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

### Function Signature

```python
def highest_scoring_word(s: str) -> str:
    """
    Returns the highest scoring word from a string.
    :param s: The input string.
    :type s: str
    :return: The highest scoring word.
    :rtype: str
    """
    # Implementation of the function goes here
```

### Examples

```python
highest_scoring_word('man i need a taxi up to ubud') # 'taxi'
highest_scoring_word('what time are we climbing up the volcano') # 'volcano'
highest_scoring_word('take me to semynak') # 'semynak'
```

### Constraints

- The input string will only contain lowercase letters and spaces. It can not include numbers, special characters, or punctuation.

### Hints

- You can use the `split` method to separate the words.
- You can use the `sum` method to calculate the score for each word.
- 
## Solutions

<details>
  <summary>Click For Solution 1</summary>

```python
def highest_scoring_word(s):
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
```

</details>

<details>
  <summary>Click For Solution 2</summary>

```python
def highest_scoring_word(s: str) -> str:
    # Split the sentence by space
    words = s.split(' ')

    # map the array of words to an array of scores
    scores = [sum(ord(letter) - ord('a') + 1 for letter in word) for word in words]

    highest_score = max(scores)
    highest_index = scores.index(highest_score)

    return words[highest_index]
```

## Explanation

- Split the input string into an array of words using the `split` method.
- Use the `sum` method to calculate the score for each word in the inner for loop of words
- Find the highest score using the `max` method.
- Find the index of the word with the highest score using the `index` method.
- Return the word with the highest score using the `highest_index`.

</details>

### Test Cases

```python
import highest_scoring_word as h


def test_find_the_highest_scoring_word():
    assert h.highest_scoring_word('hello my name is xavier') == 'xavier'
    assert h.highest_scoring_word('what time are we climbing up the volcano') == 'volcano'
    assert h.highest_scoring_word('take me to semynak') == 'semynak'
```

Remember to use the provided test cases to verify your solution
