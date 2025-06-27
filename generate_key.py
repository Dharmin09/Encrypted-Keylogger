from cryptography.fernet import Fernet

def generate_key():
    """Generate a new Fernet key."""
    print(Fernet.generate_key().decode())

if __name__ == "__main__":
    generate_key()
