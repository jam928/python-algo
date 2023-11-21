import reverse_string as rs
import pytest

def test_reverse_string():
    assert rs.reverse_string("Hello") == 'olleH'
    assert rs.reverse_string("JavaScript") == 'tpircSavaJ'
    assert rs.reverse_string("12345") == '54321'
