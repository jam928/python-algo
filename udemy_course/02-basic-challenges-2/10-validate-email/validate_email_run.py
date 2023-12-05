import validate_email as validate

result1 = validate.validate_email('joe@gmail.com')
result2 = validate.validate_email('joegmailcom')

print(result1, result2)