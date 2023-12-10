def is_valid_ipv4(input_str):
  # Split the input string into an array of octets.
  octets = input_str.split('.')

  # If the input string does not contain exactly 4 octets, return False.
  if len(octets) != 4:
    return False

  # Otherwise, return True if every octet is a number between 0 and 255.
  return all(0 <= int(octet) <= 255 and octet == str(int(octet)) for octet in octets)


# Example usage:
result = is_valid_ipv4("123.045.067.089")
print(result)

