from passlib.context import CryptContext

# 1. Initialize the Bcrypt hashing engine
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """Runs the plain text password through the Bcrypt woodchipper."""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Compares the new sawdust to the saved sawdust."""
    return pwd_context.verify(plain_password, hashed_password)