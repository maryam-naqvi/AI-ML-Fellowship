import base64

def encrypt_password(password):
    """Encodes the password to Base64 to hide it from plain text."""
    password_bytes = password.encode("ascii")
    base64_bytes = base64.b64encode(password_bytes)
    return base64_bytes.decode("ascii")

def decrypt_password(encrypted_password):
    """Decodes the Base64 string back to the original password."""
    base64_bytes = encrypted_password.encode("ascii")
    password_bytes = base64.b64decode(base64_bytes)
    return password_bytes.decode("ascii")