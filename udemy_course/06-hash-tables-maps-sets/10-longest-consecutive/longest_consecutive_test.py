from longest_consecutive import longest_consecutive_sequence


def test_longest_consecutive_sequence():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 9, 1]) == 10
