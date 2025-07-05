import cv2
import numpy as np
import time
import os
from datetime import datetime
from mss import mss

# Constants
FPS = 20
CHUNK_DURATION = 30  # seconds
CODEC = 'XVID'  # or 'MJPG'

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def get_video_writer(output_dir, width, height, screen_id):
    timestamp = get_timestamp()
    filename = os.path.join(output_dir, f'screen{screen_id}_{timestamp}.avi')
    fourcc = cv2.VideoWriter_fourcc(*CODEC)
    writer = cv2.VideoWriter(filename, fourcc, FPS, (width, height))
    return writer, filename

def record_single_monitor(output_dir, monitor, screen_id):
    width = monitor['width']
    height = monitor['height']
    sct = mss()

    writer, _ = get_video_writer(output_dir, width, height, screen_id)
    start_time = time.time()

    try:
        while True:
            img = sct.grab(monitor)
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            writer.write(frame)

            if time.time() - start_time >= CHUNK_DURATION:
                writer.release()
                writer, _ = get_video_writer(output_dir, width, height, screen_id)
                start_time = time.time()

            time.sleep(1 / FPS)

    except Exception:
        writer.release()

def record_all_screens(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    monitors = mss().monitors[1:]  # Skip the [0] virtual full-screen
    import threading

    for i, monitor in enumerate(monitors, start=1):
        t = threading.Thread(target=record_single_monitor, args=(output_dir, monitor, i))
        t.daemon = True
        t.start()
