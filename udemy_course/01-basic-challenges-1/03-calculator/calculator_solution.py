def calculate(num1, num2, operator):
    # Declare a variable to store the result
    result = None

    # Use if/elif/else statements to determine which operation to perform
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        # If the operator is not one of the above, raise an error
        raise ValueError('Invalid operator')

    return result
