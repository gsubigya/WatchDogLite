import os
import sys
import traceback
import datetime
import socket
import subprocess
import winreg
import atexit

LOCKFILE = os.path.join(os.getenv("TEMP"), "sys_monitor_lockfile.lock")

def is_already_running():
    try:
        if os.path.exists(LOCKFILE):
            return True
        with open(LOCKFILE, 'w') as f:
            f.write(str(os.getpid()))
        atexit.register(lambda: os.remove(LOCKFILE))
        return False
    except Exception as e:
        log_error(f"Error checking if the app is already running: {e}")
        return False

def log_error(message, folder=None):
    _log("ERROR", message, folder, traceback.format_exc())

def log_info(message, folder=None):
    _log("INFO", message, folder)

def _log(level, message, folder, extra=""):
    try:
        log_path = os.path.join(folder or ".", "silentlog.txt")
        with open(log_path, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {level}: {message}\n")
            if extra:
                f.write(extra + "\n")
    except Exception as e:
        log_error(f"Failed to write log: {e}", folder)

def register_startup(app_name, exe_path):
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0, winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        log_error(f"Failed to add app to startup: {e}")
        return False

def log_ip_and_domains(folder):
    try:
        ip = socket.gethostbyname(socket.gethostname())
        log_info(f"Device IP Address: {ip}", folder)

        output = subprocess.check_output("netstat -n", shell=True).decode()
        domains = set()
        for line in output.splitlines():
            if "ESTABLISHED" in line or "TIME_WAIT" in line:
                parts = line.split()
                if len(parts) >= 3:
                    domains.add(parts[2].split(':')[0])
        for d in domains:
            log_info(f"Visited IP/Domain: {d}", folder)
    except Exception as e:
        log_error(f"Failed to fetch IP/domain info: {e}", folder)
