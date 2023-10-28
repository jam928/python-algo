import count_occurrences


def test_count_occurrences_of_a_character():
    assert count_occurrences.count("hello", "l") == 2
    assert count_occurrences.count("programming", "m") == 2
    assert count_occurrences.count("banana", "a") == 3
