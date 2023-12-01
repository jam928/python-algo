import find_missing_letter as fml


def test_find_missing_letter():
    assert fml.find_missing_letter(['a', 'b', 'c', 'e']) == 'd'
    assert fml.find_missing_letter(['X', 'Z']) == 'Y'
    assert fml.find_missing_letter(['m', 'n', 'o', 'q', 'r']) == 'p'
    assert fml.find_missing_letter(['F', 'G', 'H', 'J']) == 'I'
