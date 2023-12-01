def find_missing_letter(arr):
    # Find the char code of the first letter in the array
    start = ord(arr[0])

    # Loop through the array
    for i in range(1, len(arr)):
        # Find the char code of the current letter in the array
        current = ord(arr[i])

        # If the difference between the current char code and the start char code is greater than 1, return the letter that is missing
        if current - start > 1:
            # Convert the char code to a letter
            return chr(start + 1)

        # Update the start char code
        start = current

    # If no letter is missing, return an empty string
    return ''
