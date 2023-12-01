import find_missing_number as fmn


def test_finding_the_missing_number():
    assert fmn.find_missing_number([1, 2, 3, 5]) == 4
    assert fmn.find_missing_number([10, 8, 6, 7, 5, 4, 2, 3, 1]) == 9
    assert fmn.find_missing_number([1, 3, 4, 5, 6]) == 2
