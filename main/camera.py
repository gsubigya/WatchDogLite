import cv2
import time
import os
from datetime import datetime

class CameraCapture:
    def __init__(self, config):
        self.photo_dir = config.photo_dir
        self.interval = config.photo_interval

    def run(self):
        while True:
            try:
                filename = datetime.now().strftime("photo_%Y%m%d_%H%M%S.jpg")
                filepath = os.path.join(self.photo_dir, filename)

                cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                ret, frame = cam.read()
                if ret:
                    cv2.imwrite(filepath, frame)
                cam.release()
                time.sleep(self.interval)
            except:
                time.sleep(self.interval)
