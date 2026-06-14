from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print("\n=== COPY THE TEXT BELOW ===")
print(pwd_context.hash("admin123"))
print("===========================\n")