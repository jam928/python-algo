def validate_password(password: str):
    is_length_valid = len(password) >= 8
    contains_lowercase_character = any(c.islower() for c in password)
    contains_uppercase_character = any(c.isupper() for c in password)
    contains_digit = any(c.isdigit() for c in password)

    return is_length_valid and contains_uppercase_character and contains_lowercase_character and contains_digit
