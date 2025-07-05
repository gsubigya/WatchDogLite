import os
import json
from tkinter import Tk, filedialog

class Config:
    def __init__(self):
        self.config_path = os.path.join(os.getenv("APPDATA"), "sys_monitor_config.json")
        self.base_folder = self._load_or_select_folder()

        self.video_dir = os.path.join(self.base_folder, "videos")
        self.log_dir = os.path.join(self.base_folder, "logs")
        self.photo_dir = os.path.join(self.base_folder, "photos")

        self.photo_interval = 120       # seconds
        self.video_chunk_length = 300   # seconds
        self.app_name = "SystemMonitor"
        self.exe_path = os.path.abspath(__file__).replace(".py", ".exe")

        self._create_folders()

    def _load_or_select_folder(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    return json.load(f).get("base_folder")
            except Exception:
                pass  # fallback to asking again

        try:
            root = Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            folder = filedialog.askdirectory(title="Select folder to save monitoring data")
            root.destroy()
        except Exception as e:
            raise RuntimeError(f"Failed to show folder selection dialog: {e}")

        if not folder:
            raise FileNotFoundError("Monitoring folder not selected.")

        with open(self.config_path, "w") as f:
            json.dump({"base_folder": folder}, f)
        return folder

    def _create_folders(self):
        os.makedirs(self.video_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.photo_dir, exist_ok=True)
