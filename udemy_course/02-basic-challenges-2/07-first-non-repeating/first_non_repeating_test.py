import first_non_repeating as fnr


def test_find_first_non_repeating_character():
    assert fnr.find_first_non_repeating_character("aabccdeff") == "b"
    assert fnr.find_first_non_repeating_character("aabbcc") is None
    assert fnr.find_first_non_repeating_character("hello world") == "h"
