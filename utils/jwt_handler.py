import jwt
from datetime import datetime, timedelta

SECRET_KEY = "MY_SUPER_SECRET_KEY"   # you can change
ALGORITHM = "HS256"


def create_access_token(email: str):
    """
    Create JWT token valid for 1 hour.
    """
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token: str):
    """
    Verify JWT and return email if valid.
    """
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return data["sub"]
    except Exception:
        return None
