import find_max_number
import pytest
def test_find_max_number_in_array():
  assert find_max_number.find_max([1, 5, 3, 9, 2]) == 9
  assert find_max_number.find_max([0, -1, -5, 2]) == 2
  assert find_max_number.find_max([10, 10, 10, 10]) == 10