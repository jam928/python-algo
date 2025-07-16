import secrets
import base64

def generate_random_key(length=32):
    key = secrets.token_bytes(length)
    return base64.b64encode(key).decode('utf-8')

print(generate_random_key())