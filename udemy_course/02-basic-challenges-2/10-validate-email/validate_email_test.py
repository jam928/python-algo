import validate_email as valid_email


def test_email_addresses():
    valid_email_addresses = ['john@example.com', 'jane.doe@domain.org']

    for email in valid_email_addresses:
        assert valid_email.validate_email(email) is True

    invalid_email_addresses = ['invalid-email', '@domain.com', 'user@domain']

    for email in invalid_email_addresses:
        assert valid_email.validate_email(email) is False
