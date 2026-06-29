from app.config.database import SessionLocal
from app.models.staff_model import Staff 
from passlib.context import CryptContext

# Build the bcrypt hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def override_system():
    db = SessionLocal()
    
    print("Initiating God-Mode Override...")
    
    try:
        # 1. Hash the password
        secure_password = pwd_context.hash("admin123")
        
        # 2. Create the VIP Admin object using your exact column names
        rescue_admin = Staff(
            username="BhanuAdmin",
            hashed_password=secure_password, 
            role="Admin"
        )
        
        # 3. Inject it into MySQL
        db.add(rescue_admin)
        db.commit()
        print("✅ SYSTEM OVERRIDE SUCCESSFUL: Admin account injected!")
        print("👉 You may now log in with -> Username: BhanuAdmin | Password: admin123")
        
    except Exception as e:
        print(f"❌ Override failed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    override_system()