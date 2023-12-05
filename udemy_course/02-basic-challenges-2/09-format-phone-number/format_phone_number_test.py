import format_phone_number as format


def test_format_phone_number():
    assert format.format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == '(123) 456-7890'
    assert format.format_phone_number([5, 0, 2, 4, 8, 1, 9, 6, 3, 7]) == '(502) 481-9637'
    assert format.format_phone_number([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == '(999) 999-9999'
