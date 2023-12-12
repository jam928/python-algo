def find_missing_letter(arr):
    # create a list of char codes for each letter in the array
    char_codes = [ord(letter) for letter in arr]

    # find the missing letter using list comprehension return the current character plus one;
    # if the char code of the next one difference with the current char is greater than 1
    missing_letter = next((chr(char_codes[i] + 1) for i in range(len(char_codes)) if char_codes[i+1] - char_codes[i] > 1), "")

    return missing_letter
