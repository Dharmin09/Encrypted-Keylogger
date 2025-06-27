import requests, os
from core.encryptor import encrypt_data

def get_geolocation():
    """Fetch and encrypt public IP-based geolocation."""
    try:
        # Fetch geolocation info based on public IP
        res = requests.get("http://ip-api.com/json/")
        geo_data = res.text.encode("utf-8")  # Convert string to bytes

        # Make sure the directory exists
        os.makedirs(".logs/geolocation", exist_ok=True)

        # Write encrypted geolocation data to a file
        with open(".logs/geolocation/geo.txt", "wb") as f:
            f.write(encrypt_data(geo_data))

    except Exception as e:
        print("[!] Geolocation error:", e)
