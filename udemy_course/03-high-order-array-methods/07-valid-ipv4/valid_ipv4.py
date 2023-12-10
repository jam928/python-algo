def is_valid_ipv4(input_str: str) -> bool:
    octets = input_str.split(".")
    return len(octets) == 4 and all(0 <= int(octet) <= 255 and octet == str(int(octet)) for octet in octets)
