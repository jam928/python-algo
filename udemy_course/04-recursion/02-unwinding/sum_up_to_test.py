import sum_up_to as s


def test_sum_up_positive_integers():
    assert s.sum_up_to(5) == 15
    assert s.sum_up_to(10) == 55
    assert s.sum_up_to(1) == 1
    assert s.sum_up_to(0) == 0
