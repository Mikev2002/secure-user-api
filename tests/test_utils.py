from app.utils.security import hash_password, verify_password

def test_password_hash_and_verify():
    raw = "securepass123"
    hashed = hash_password(raw)
    
    assert hashed != raw  # Password should be hashed
    assert verify_password(raw, hashed)  # Hashed password should verify
