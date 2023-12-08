import valid_anagrams as v


def test_valid_anagrams():
    assert v.valid_anagrams('listen', 'silent') is True
    assert v.valid_anagrams('hello', 'world') is False
    assert v.valid_anagrams('astronomer', 'moonstarer') is True
    assert v.valid_anagrams('apple', 'banana') is False
