# Challenge: Word Frequency Counter

## Instructions

Write a function called `word_frequency_counter` that takes a string as input and returns a map that represents the frequency of each word in the string. We did a similar challenge way back that counted the occurrences of a character. This function should count the occurrences of each word, ignoring case and excluding punctuation.

### Function Signature

```python
from collections import defaultdict

def word_frequency_counter(s):
    """
    Returns a dictionary that represents the frequency of each word in the input string.
    
    Parameters:
    - s (str): The input string containing words.
    
    Returns:
    - dict: The dictionary with word frequency.
    """
    # Your code here

```

### Examples

```python
word_frequency_counter('The quick brown fox jumps over the lazy dog.')
# Output: Map { 'the' => 2, 'quick' => 1, 'brown' => 1, 'fox' => 1, 'jumps' => 1, 'over' => 1, 'lazy' => 1, 'dog' => 1 }

word_frequency_counter(
  'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
)
# Output: Map { 'lorem' => 1, 'ipsum' => 1, 'dolor' => 1, 'sit' => 1, 'amet' => 1, 'consectetur' => 1, 'adipiscing' => 1, 'elit' => 1 }
```

### Constraints

- The input string will only contain letters, spaces, and punctuation marks.

### Hints

- You can use the `toLowerCase()` method to convert the input string to lowercase, so you can ignore the case when counting word frequency.
- Regular expressions can be helpful for splitting the string into words and removing punctuation marks.
- You can use a map to store the word frequencies, where the word is the key, and the count is the value. Loop through each word, update the count in the map, and return the final map.

### Solutions

<details>
  <summary>Click For Solution</summary>

```python
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
```

### Explanation

- Create a variable `words` to store the lowercase version of the input string, split into an array of words. The regular expression `/W+/` matches one or more non-word characters, which includes spaces and punctuation marks. This will split the string into an array of words, ignoring spaces and punctuation marks.

- Create an empty `Map` called `wordFrequency` to store the word frequencies.

- Iterate through each word in the array. If the word is an empty string (which can be caused by multiple spaces or punctuation marks), skip it using `continue`. Otherwise, we check if the word is already in the map.
- If it is, we increment its frequency by 1. If it's not in the map, we add it to the map with a frequency of 1.
- Return the `wordFrequency` map, which contains the frequency of each word in the input string.

</details>

### Test Cases

```python
from word_frequency_counter import word_frequency_counter


def test_word_frequency_counter():
    input_text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."
    expected_output = {
        'the': 4,
        'quick': 1,
        'brown': 1,
        'fox': 2,
        'jumps': 1,
        'over': 1,
        'lazy': 1,
        'dog': 2,
        'barks': 1,
        'and': 1,
        'runs': 1,
        'away': 1,
    }

    result = word_frequency_counter(input_text)
    assert result == expected_output


def test_word_frequency_counter_empty_input():
    input_text = ''
    expected_output = {}

    result = word_frequency_counter(input_text)
    assert result == expected_output


def test_word_frequency_counter_single_word():
    input_text = 'hello'
    expected_output = {
        'hello': 1,
    }

    result = word_frequency_counter(input_text)
    assert result == expected_output

```
