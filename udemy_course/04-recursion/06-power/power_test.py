from power import power


def test_calculate_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(3, 4) == 81
