def are_all_characters_unique(s):
  """
  Returns True if all characters in a string are unique.
  :param s: The string to check.
  :type s: str
  :return: Whether all characters in the string are unique.
  :rtype: bool
  """
  # Create a new set
  char_set = set()

  # Loop through the string
  for char in s:
    # If the set already has the current character, return False
    if char in char_set:
      return False
    # Add the current character to the set
    char_set.add(char)

  # If no characters are repeated, return True
  return True

def are_all_characters_unique_2(s):
  """
  Returns True if all characters in a string are unique.
  :param s: The string to check.
  :type s: str
  :return: Whether all characters in the string are unique.
  :rtype: bool
  """
  # Create a dictionary to keep track of the characters in the string
  char_count = {}

  # Loop through the string
  for char in s:
    # If the character is already in the dictionary, return False
    if char_count.get(char):
      return False
    # Add the current
    char_count.update({char: True})

  return True