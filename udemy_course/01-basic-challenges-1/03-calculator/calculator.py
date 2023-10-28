def calculate(num1, num2, operator):
    cases = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }
    result = cases.get(operator)

    return result