from cryptography.fernet import Fernet

def generate_key():
    """Generate and print a new Fernet encryption key."""
    key = Fernet.generate_key()
    print(f"[+] Generated Key: {key.decode()}")

if __name__ == "__main__":
    generate_key()
