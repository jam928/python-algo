import password_validator as pv

result1 = pv.validate_password("Abc12345")
result2 = pv.validate_password("password")

print(result1, result2)