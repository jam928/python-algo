def format_phone_number(numbers):
    # Get the first 3 numbers and join them together
    area_code = ''.join(map(str,numbers[0:3]))

    # Get the next 3 numbers and join them together
    prefix = ''.join(map(str,numbers[3:6]))

    # Get the last 4 numbers and join them together
    line_number = ''.join(map(str,numbers[6:]))

    return f"({area_code}) {prefix}-{line_number}"