import cv2
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import time

class Camera(QThread):
    img_changed = Signal(bytes)

    def __init__(self, capture_device=None, width=420, height=640, running=False, parent=None):
        super().__init__(parent)
        self.capture_device = capture_device
        self.current_frame = None
        self.running = running
        self.width = width
        self.height = height

        self.capture_indices = self.scan_capture_indices()
        self._live = False
        self._recording = False
        self.live_feed = None

    def run(self):
        while self.running and self.capture_device.isOpened():
            ret, frame = self.capture_device.read()

            if ret is True:
                h, w, ch = frame.shape

                bytes_per_line = ch * w
                qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                scaled_img = qt_image.scaled(self.width, self.height, Qt.KeepAspectRatio)
                pix_map = QPixmap.fromImage(scaled_img)
                self.img_changed.emit(pix_map)

        if self.capture_device.isOpened():
            self.capture_device.release()
        print("cam thread reached end")

    def scan_capture_indices(self, captures_to_try=3):
        indices = []
        for i in range(0, captures_to_try):
            try:
                c = cv2.VideoCapture(i)
                if c.isOpened():
                    indices.append(i)
                c.release()
            except Exception as e:
                print(e)

        return indices

    def set_live_mode(self):
        self._live = True
        self._recording = False

    def enable_rec_mode(self):
        self._recording = True
        self._live = False

    def set_capture_device(self, cap_index, res_width=1280, res_height=1024):
        if self.capture_device is not None:
            self.capture_device.release()
        self.capture_device = cv2.VideoCapture(cap_index)
        self.capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, int(res_width))
        self.capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, int(res_height))

