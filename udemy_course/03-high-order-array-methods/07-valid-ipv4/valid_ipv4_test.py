import valid_ipv4 as v


def test_valid_ipv4_addresses():
    ipv4_addresses = {
        '1.2.3.4': True,
        '123.45.67.89': True,
        '1.2.3': False,
        '1.2.3.4.5': False,
        '123.456.78.90': False,
        '123.045.067.089': False
    }

    for e in ipv4_addresses:
        assert v.is_valid_ipv4(e) is ipv4_addresses[e]
