from datetime import datetime, timedelta
from jose import JWTError, jwt

# Secret key to encode/decode JWT (use a secure one in production!)
SECRET_KEY = "your-secret-key"  # replace with a strong secret key or move to .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create a new JWT token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    """Decode JWT token and return payload."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def verify_token(token: str):
    """Verify and extract username (sub) from JWT."""
    payload = decode_access_token(token)
    if not payload:
        return None
    username = payload.get("sub")
    return username
