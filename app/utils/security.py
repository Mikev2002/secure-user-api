from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# 🔐 Set up the password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔑 JWT Config
SECRET_KEY = "super-secret-key"  # ⛔️ Replace this with a secure env variable in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ✅ Hash a plain password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# ✅ Verify a password against a hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ✅ Create a JWT access token
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
