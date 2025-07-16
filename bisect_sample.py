from bisect import bisect_left

def find_insertion_point(sorted_list, value):
  """
  Finds the insertion point for a value in a sorted list using bisect_left.

  Args:
    sorted_list: A sorted list of comparable elements.
    value: The value to find the insertion point for.

  Returns:
    The index where the value should be inserted to maintain the sorted order.
  """
  
  return bisect_left(sorted_list, value)

# Example usage:
my_list = [2, 5, 5, 8, 12]
value_to_insert = 5
index = find_insertion_point(my_list, value_to_insert)
print(f"The value {value_to_insert} should be inserted at index: {index}")

value_to_insert = 7
index = find_insertion_point(my_list, value_to_insert)
print(f"The value {value_to_insert} should be inserted at index: {index}")

value_to_insert = 15
index = find_insertion_point(my_list, value_to_insert)
print(f"The value {value_to_insert} should be inserted at index: {index}")