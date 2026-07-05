import bcrypt

def hash_password(password):
    """
    Hash a plain text password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def verify_password(password, hashed_password):
    """
    Verify a plain text password against a hashed password.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password) 