from phone_number_directory import phone_number_directory

phone_numbers = [
  'John:123-456-7890',
  'Jane:987-654-3210',
  'Joe:555-555-5555',
]

result = phone_number_directory(phone_numbers)

print(result.get('John'))