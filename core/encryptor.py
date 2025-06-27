from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ENCRYPTION_KEY")
fernet = Fernet(key.encode())

def encrypt_data(data: bytes) -> bytes:
    """Encrypt bytes using Fernet key."""
    return fernet.encrypt(data)

def decrypt_data(token: bytes) -> bytes:
    """Decrypt bytes using Fernet key."""
    return fernet.decrypt(token)
