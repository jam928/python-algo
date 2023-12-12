import reverse_string_recursion as r


def test_reverse_a_string():
    assert r.reverse_string("Hello") == 'olleH'
    assert r.reverse_string("JavaScript") == 'tpircSavaJ'
    assert r.reverse_string("12345") == '54321'
