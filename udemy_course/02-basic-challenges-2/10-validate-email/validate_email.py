def validate_email(email):
    if '@' not in email:
        return False

    [local_part, domain] = email.split('@')

    # if the length of the first part of the email is 0 or length of the domain is less than 3
    # return false as does not mean the requirements of a valid email
    if len(local_part) == 0 or len(domain) < 3:
        return False

    domain_extension = domain.split('.')

    if len(domain_extension) < 2 or len(domain_extension[1]) < 2:
        return False

    return True
