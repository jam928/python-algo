import re


def validate_email(email):
    """
    Returns whether the string is a valid email address.
    :param email: The email address to validate.
    :type email: str
    :return: Whether the email address is valid.
    :rtype: bool
    """
    # Regular expression for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Using re.match() to check if the email matches the pattern
    match = re.match(pattern, email)

    # Return True if there is a match, otherwise, return False
    return bool(match)


def validate_email_2(email):
    if '@' not in email:
        return False

    [local_part, domain] = email.split('@')

    # if the length of the first part of the email is 0 or length of the domain is less than 3
    # return false as does not mean the requirments of a valid email
    if len(local_part) == 0 or len(domain) < 3:
        return False

    domain_extension = domain.split('.')

    if len(domain_extension) < 2 or len(domain_extension[1]) < 2:
        return False

    return True
