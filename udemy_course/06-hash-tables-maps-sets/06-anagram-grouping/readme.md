# Challenge: Anagram Grouping

Anagrams are words or phrases formed by rearranging the letters of another word or phrase. For example, `cinema` is an anagram of `iceman`.

## Instructions

Write a function called `anagram_grouping` that takes an array of strings as input and returns an array of arrays, where each sub-array contains words that are anagrams of each other.

### Function Signature

```python
from typing import List

def anagram_grouping(words: List[str]) -> List[List[str]]:
    """
    Returns an array of arrays, where each sub-array contains words that are anagrams of each other.

    Parameters:
    - words (List[str]): The input list of strings containing words.

    Returns:
    - List[List[str]]: The list of lists with anagram groups.
    """
    # Your code here
```

### Examples

```python
anagram_grouping(['cat', 'act', 'dog', 'god', 'tac'])
# Output: [['cat', 'act', 'tac'], ['dog', 'god']]

anagram_grouping(['listen', 'silent', 'enlist', 'hello', 'world'])
# Output: [['listen', 'silent', 'enlist'], ['hello'], ['world']]
```

### Constraints

- The input array `words` will contain only lowercase alphabetical characters.

### Hints

- You can use a map to store the anagram groups, where the key is the sorted characters of each word, and the value is an array of words that have the same sorted characters
- You can sort a string by splitting it into an array of chars and calling `.sort()` and then `join()` it back to a string
- You can use `Array.from()` to convert a map to an array

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
from typing import List

def anagram_grouping(words: List[str]) -> List[List[str]]:

    anagram_map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams_list = anagram_map.get(sorted_word, [])
        anagrams_list.append(word)
        anagram_map.update({sorted_word: anagrams_list})

    return list(anagram_map.values())
```

### Explanation

- Create a new map `anagram_map` to store the anagram groups.
- Iterate through each word in the input array `words`. For each word, split its characters into an array, sort the array in ascending order, and then join the sorted characters back into a string. This sorted string becomes the key for our `anagram_map` map.
- Check if the key already exists in the map. If it does, retrieve the corresponding array and add the word to it.
- If the key does not exist in the map, create a new array with the word as the first element and add it to the map with the key.
- After processing all the words, extract the arrays of anagram groups from the `anagram_map` map using `list(anagram_map.values())` and return them as the final output.

</details>

### Test Cases

``` python
from anagram_grouping import anagram_grouping

def test_anagram_grouping():
    result1 = anagram_grouping(['cat', 'act', 'dog', 'god', 'tac'])
    result2 = anagram_grouping(['listen', 'silent', 'enlist', 'hello', 'world'])

    assert result1 == [['cat', 'act', 'tac'], ['dog', 'god']]
    assert result2 == [['listen', 'silent', 'enlist'], ['hello'], ['world']]

```
