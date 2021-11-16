
from hashlib import sha256

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA256.
    """
    return sha256(password.encode()).hexdigest()
# end def

def check_password(password: str, hashed: str) -> bool:
    """
    Checks if a password matches a hashed password.
    """
    return hash_password(password) == hashed
# end def

