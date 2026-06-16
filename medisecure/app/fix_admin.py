from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print("\n=== COPY THE TEXT BELOW ===")

# Change the password here to nurse123
print(pwd_context.hash("nurse123")) 

print("===========================\n")