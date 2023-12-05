def format_phone_number_1(numbers):
    # Get the first 3 numbers and join them together
    area_code = ''.join(map(str,numbers[0:3]))

    # Get the next 3 numbers and join them together
    prefix = ''.join(map(str,numbers[3:6]))

    # Get the last 4 numbers and join them together
    line_number = ''.join(map(str,numbers[6:]))

    return f"({area_code}) {prefix}-{line_number}"


def format_phone_number_2(numbers):
    # Join all the numbers together
    formatted = ''.join(map(str,numbers))

    return f"({formatted[0:3]}) {formatted[3:6]}-{formatted[6:]}"


def format_phone_number_3(numbers):
    formatted_number = f"({''.join(map(str, numbers[:3]))}) {''.join(map(str, numbers[3:6]))}-{''.join(map(str, numbers[6:]))}"
    return formatted_number
