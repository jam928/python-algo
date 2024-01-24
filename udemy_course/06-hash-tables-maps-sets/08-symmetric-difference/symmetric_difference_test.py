from symmetric_difference import symmetric_difference

def test_symmetric_difference():
    assert symmetric_difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert symmetric_difference([1, 2, 2, 3, 4], [2, 3, 3, 4, 5]) == [1, 5]
    assert symmetric_difference([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == []
    assert symmetric_difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
