# auth/security.py — Hash de contraseña
# Version 1.0.0 WilsonGuillermo

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
