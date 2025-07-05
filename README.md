# Watchdog Lite

> A simple desktop activity tracker records screen, logs keystrokes, and monitors network activity designed for personal awareness and device monitoring.

**Watchdog Lite** is a lightweight tool built using Python that helps you keep an eye on your own system whether you're trying to understand your usage patterns, monitor for suspicious activity, or just want more visibility over your machine when you're away.

It captures your screen in short 10-second video clips, logs every keystroke, tracks visited IP addresses and domains, and can run silently from startup when converted to an executable. The intent is simple: personal peace of mind. It's built ethically and modularly to support upcoming features like webcam capture, remote logging, and encrypted storage.

⚠️ This project is intended strictly for **ethical, educational, and personal use**. I do **not support or take responsibility** for any misuse. Use it responsibly.

---

### ✅ Features

- Records screen in high-quality 10-second video segments  
- Logs keystrokes in the background  
- Captures visited domains and IP addresses  
- Can run silently on system startup (EXE version)  
- Easily converted into a standalone `.exe` for Windows  

---

### 📁 Folder Structure
watchdog-lite/
├── camera/ # Webcam functionality (planned for future)
├── config/ # Configuration and environment settings
├── installer/ # Scripts for startup integration and EXE handling
├── logger/ # Keylogging and IP/domain logging
├── recorder/ # Screen recording logic
├── utils/ # Helper scripts and utilities
├── main.py # Central script that ties all modules together


---

### 🛠️ How to Use

Make sure Python 3 is installed.

**Clone the repository**  
```bash
git clone https://github.com/yourusername/watchdog-lite.git
cd watchdog-lite

pip install -r requirements.txt

python main.py
```

### Convert to EXE (Optional for Windows)
You can convert this project into a standalone executable so it runs without needing Python installed:

Install Pyinstall
```bash
pip install pyinstaller

pyinstaller --onefile --noconsole main.py

```

The generated executable will appear in the dist/ folder. You can place this .exe in any system and configure it to run on startup via your installer/ script or manually using the Windows Startup folder.

### 🔮 Future Plans
1. Webcam snapshot capture (with configurable intervals)
2. Remote logging to a C2 or personal server
3. Encrypted local log files
4. User interface for enabling/disabling features
5. Obfuscation and stealth improvements
6. Suspicious login alerts or file tamper detection


### 🧠 Why I Built This
I’ve always been paranoid about leaving my device unattended especially in public or even semi-private spaces. It doesn’t take much just a bootable pendrive, and anyone can bypass your system password. That reality never felt safe to me.

It made me feel like someone could be watching or messing with my system at any time. So instead of living with that paranoia, I decided to build a personal watchdog. A system that watches for me when I’m not around.

This started out as a small keylogger experiment, but building a working, high-quality screen recorder that captures and stores activity in intervals was a learning curve. I kept everything modular with folders like camera/, recorder/, logger/, and config/ because I plan to evolve this into a full monitoring suite for personal devices possibly with remote access, encryption, and smart alerts.

This project has helped me learn a lot about real-time logging, system monitoring, and security. I hope it brings the same sense of control and learning to anyone who uses it.

### ⚠️ Disclaimer
This tool is developed strictly for ethical, educational, and personal use only. You must not use this tool to spy on others, access unauthorized systems, or monitor devices without clear, informed consent. Any action taken with this tool is solely your responsibility.

The developer of Watchdog Lite does not condone nor take any liability for misuse of the software in any form.

### 📬 Feedback and Contributions
If you find this project useful or have ideas for improvements, feel free to open an issue, fork the project, or contribute through pull requests. Feature ideas, bug fixes, and even documentation edits are all welcome.

Stay aware. Stay secure. 🙏
