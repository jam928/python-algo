import are_all_characters_unique as char_unique


def test_unique_characters_in_a_string():
    assert char_unique.are_all_characters_unique('abcdefg') is True
    assert char_unique.are_all_characters_unique('abcdefgA') is True
    assert char_unique.are_all_characters_unique('programming') is False
    assert char_unique.are_all_characters_unique('') is True
    assert char_unique.are_all_characters_unique('a') is True
