from typing import Union


def generate_hashtag(s: str) -> Union[str, bool]:
    # Split the string into an array of words.
    # Capitalize each word in the split and then join it with a ''
    # Concat with #
    hashtag = '#' + ''.join(word.capitalize() for word in s.split())

    # If the hashtag is only one character long or longer than 140 characters, return False, otherwise return the hashtag.
    return False if len(hashtag) == 1 or len(hashtag) > 140 else hashtag
