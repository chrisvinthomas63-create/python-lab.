# Mini Project: OTP Generator
import random
import time

def generate_otp(length=6):
    """Generate a random numeric OTP of specified length."""
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

def simulate_otp_system():
    """Simulate an OTP generation and verification system."""
    print("=" * 50)
    print("Mini Project: OTP Generator & Verification System")
    print("=" * 50)
    
    # Generate OTP
    otp = generate_otp(6)
    print(f"\n📱 Your OTP is: {otp}")
    print("(In a real system, this would be sent via SMS/Email)")
    
    # Simulate OTP expiry (optional)
    print("\n⏳ This OTP will expire in 30 seconds...")
    
    # Get user input
    user_otp = input("\nEnter the OTP to verify: ").strip()
    
    # Verify OTP
    if user_otp == otp:
        print("\n✅ OTP Verified Successfully!")
    else:
        print("\n❌ Invalid OTP. Access Denied.")

if __name__ == "__main__":
    simulate_otp_system()