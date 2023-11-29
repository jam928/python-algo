import remove_duplicates as rd


def test_remove_duplicates_from_array():
    assert rd.remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    assert rd.remove_duplicates(['apple', 'banana', 'orange', 'banana', 'kiwi']) == ['apple', 'banana', 'orange',
                                                                                     'kiwi']
    assert rd.remove_duplicates([True, True, False, True, False]) == [True, False]
