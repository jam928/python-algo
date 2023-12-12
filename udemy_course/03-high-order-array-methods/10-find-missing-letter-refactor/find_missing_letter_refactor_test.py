import find_missing_letter_refactor as f


def test_find_missing_letter():
    assert f.find_missing_letter(['a', 'b', 'c', 'e']) == 'd'
    assert f.find_missing_letter(['X', 'Z']) == 'Y'
    assert f.find_missing_letter(['m', 'n', 'o', 'q', 'r']) == 'p'
    assert f.find_missing_letter(['F', 'G', 'H', 'J']) == 'I'
