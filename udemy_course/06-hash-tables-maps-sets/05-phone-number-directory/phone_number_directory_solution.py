def phone_number_directory(phone_numbers):
    # Create a new dictionary
    directory = {}

    # Loop through each entry in the phone_numbers list
    for entry in phone_numbers:
        # Split the entry into a name and phone number
        name, phone_number = entry.split(':')
        # Add the name and phone number to the directory
        directory[name] = phone_number

    # Return the directory
    return directory
