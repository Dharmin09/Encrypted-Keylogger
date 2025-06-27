# 🔐 Encrypted Keylogger with Data Exfiltration

This project is a **Python-based Encrypted Keylogger** designed for **educational and ethical hacking** purposes. It captures keystrokes, screenshots, webcam images, and geolocation data, encrypts them, and securely exfiltrates the data via email.

> ⚠️ **Disclaimer:** This tool is intended strictly for educational and authorized penetration testing only. Do not use it without proper consent.

---

## 📌 Features

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🔑 Keystroke Logging | Captures all keystrokes in human-readable format                            |
| 🖼️ Screenshots        | Periodically captures the current screen                                   |
| 📸 Webcam Capture     | Takes photos from the webcam at defined intervals                          |
| 🌍 Geolocation        | Gets approximate location using public IP                                  |
| 🔐 AES Encryption     | All data is encrypted before being sent                                    |
| 💌 Email Exfiltration| Encrypted logs are sent via SMTP email                                      |
| ♻️ Persistence        | Ensures the script runs on system startup via registry                     |

---

## 🧰 Tools & Libraries Used

- Python 3.x
- `pynput` – Keyboard logging
- `cryptography` – AES encryption
- `requests` – IP-based geolocation
- `opencv-python` – Webcam capture
- `Pillow` – Screenshots
- `smtplib`, `ssl` – Email sending
- `threading`, `time`, `os`, `uuid`, `platform`, `socket`, `subprocess`, `winreg`

---

## ⚙️ How to Run

1. 📁 **Directory Structure**
    ```
    ENCRYPTEDLOGGER/
    ├── core/
    │   ├── __init__.py
    │   ├── encryptor.py
    │   ├── geolocation.py
    │   ├── logger.py
    │   ├── persistence.py
    │   ├── screenshot.py
    │   └── webcam.py
    ├── send/
    │   ├── __init__.py
    │   └── mailer.py
    ├── command.txt
    ├── generate_key.py
    ├── myconfig.py
    ├── requirements.txt
    └── run_all.py
    ```

2. 📦 **Install Dependencies**

    Before running anything, install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. ✉️ **Set up Email Exfiltration**

    In `send/mailer.py`, configure:
    ```python
    EMAIL_ADDRESS = "your_email@example.com"
    EMAIL_PASSWORD = "your_app_password"
    TO_EMAIL = "receiver_email@example.com"
    ```

4. 🔐 **Generate an Encryption Key**
    ```bash
    python generate_key.py
    ```
    Then paste the generated key into `myconfig.py` like this:
    ```python
    ENCRYPTION_KEY = b'your_generated_key'
    ```

5. ▶️ **Run the keylogger**
    ```bash
    python run_all.py
    ```

6. 💻 **Control using `command.txt`**

    The script monitors `command.txt`. Based on its content, the logger reacts as follows:

    | Command in `command.txt` | Description                                                  |
    |--------------------------|--------------------------------------------------------------|
    | `START`                  | Begins logging, screenshots, webcam, and location capture    |
    | `STOP`                   | Temporarily halts logging and capture modules                |
    | `EXIT`                   | Stops the program and performs cleanup operations            |

    > 💡 `command.txt` must be in the root folder. You can edit it anytime while the program is running.

---

## 🧪 Educational Use-Cases

- Simulate how malware/keyloggers operate
- Learn secure data encryption and email exfiltration
- Practice Red Team/Blue Team scenarios
- Implement stealth persistence techniques

---

## 🛑 Disclaimer

This tool is for **authorized and ethical use only**:
- ✔️ Educational research
- ✔️ Ethical hacking with permission
- ❌ Unauthorized spying, stalking, or malicious deployment is illegal

---

## 📄 License

MIT License  
Feel free to fork and contribute, but **respect laws and ethics**.

---

## 👨‍💻 Author

**Dharmin Tank**  
**B.Tech CSE – Cybersecurity Student**  

- 🔗 GitHub: [@dharmin09](https://github.com/Dharmin09)  
- 🔗 LinkedIn: [linkedin.com/in/dharmin09](https://linkedin.com/in/dharmin09)  
- 📧 Email: dharmintank09@gmail.com  
