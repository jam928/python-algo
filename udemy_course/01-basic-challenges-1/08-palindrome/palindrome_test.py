import palindrome as pd


def test_palindrome_strings():
    assert pd.is_palindrome("racecar") is True
    assert pd.is_palindrome("Hello") is False
    assert pd.is_palindrome("A man, a plan, a canal, Panama") is True
    assert pd.is_palindrome("12321") is True
