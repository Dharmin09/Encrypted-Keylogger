import requests, os
from core.encryptor import encrypt_data

def get_geolocation():
    """Fetch and encrypt public IP-based geolocation."""
    try:
        res = requests.get("http://ip-api.com/json/")
        geo_data = res.text.encode("utf-8")
        os.makedirs(".logs/geolocation", exist_ok=True)
        with open(".logs/geolocation/geo.txt", "wb") as f:
            f.write(encrypt_data(geo_data))
    except Exception as e:
        print("[!] Geolocation error:", e)
