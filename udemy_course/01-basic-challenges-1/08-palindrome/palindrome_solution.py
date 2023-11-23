# Solution 1
def is_palindrome(str):
  # Remove all non-alphanumeric characters and convert the string to lowercase
  formattedStr = str.lower().replace('/[^a-z0-9]/g', '')
  # Reverse the string
  reversedStr = formattedStr.split('').reverse().join('')
  # Return whether the formatted string is equal to the reversed string
  return formattedStr is reversedStr


# Solution 2
def is_palindrome_2(str):
  # Remove all non-alphanumeric characters and convert the string to lowercase
  formattedStr = removeNonAlphanumeric(str.toLowerCase())

  # Reverse the string
  reversedStr = reverseString(formattedStr)

  # Return whether the formatted string is equal to the reversed string
  return formattedStr is reversedStr


# Helper functions
def removeNonAlphanumeric(str):
  # Declare a variable to store the formatted string
  formattedStr = ''
  # Loop through the string
  for i in range(len(str)):
    # If the current character is alphanumeric, add it to the formatted string
    char = str[i]
    if isAlphaNumeric(char):
      formattedStr += char


  return formattedStr


def isAlphaNumeric(char):
  # Get the character code
  code = char.charCodeAt(0)
  # Return whether the character is alphanumeric
  return (
    (code >= 48 and code <= 57)or # Numbers 0-9
    (code >= 97 and code <= 122) # Lowercase letters a-z
  )


def reverseString(str):
  # Declare a variable to store the reversed string
  reversed = ''
  # Loop through the string backwards
  for i in range(len(str) - 1, -1 , -1):
    # Add each character to the reversed string
    reversed += str[i]

  # Return the reversed string
  return reversed