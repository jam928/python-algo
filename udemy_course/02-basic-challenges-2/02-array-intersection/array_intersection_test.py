import array_intersection as ai

def test_array_intersection():
  assert ai.array_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3,4,5]
  assert ai.array_intersection([10, 20, 30], [30, 40, 50]) == [30]
  assert ai.array_intersection([1, 2, 3], [4, 5, 6]) == []