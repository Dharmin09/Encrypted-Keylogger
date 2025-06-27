from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the encryption key from environment variable
key = os.getenv("ENCRYPTION_KEY")
fernet = Fernet(key.encode())

# Function to encrypt data
def encrypt_data(data: bytes) -> bytes:
    """Encrypt bytes using Fernet key."""
    return fernet.encrypt(data)

# Function to decrypt data
def decrypt_data(token: bytes) -> bytes:
    """Decrypt bytes using Fernet key."""
    return fernet.decrypt(token)
