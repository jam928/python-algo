def fizz_buzz_array(num):
    # Store the resulting fizzbuzz elements
    result = []
    for i in range(1, num+1):
        # if the current element is divisible both by 3 and 5 then append fizzbuzz
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # else if the current element is divisible both by 3 only append fizz
        elif i % 3 == 0:
            result.append("Fizz")
        # else if the current element is divisible both by 5 only append buzz
        elif i % 5 == 0:
            result.append("Buzz")
        # else append the current element
        else:
            result.append(i)

    return result