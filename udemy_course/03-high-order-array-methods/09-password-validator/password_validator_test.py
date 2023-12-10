import password_validator as pv


def test_password_validation():
    assert pv.validate_password("Abc12345") is True
    assert pv.validate_password("password123") is False
    assert pv.validate_password("Pass") is False
    assert pv.validate_password("HelloWorld") is False
