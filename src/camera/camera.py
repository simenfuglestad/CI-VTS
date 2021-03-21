import cv2
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import time


class CameraLiveFeed(QThread):
    img_changed = Signal(bytes)

    def __init__(self, camera, width=400, height=600, running=True, parent=None):
        super().__init__(parent)
        self.camera = camera
        self.current_frame = None
        self.running = running
        self.width = width
        self.height = height
        print(self.width)
        print(self.height)

    def run(self):
        self.running = True
        while self.running and self.camera is not None:
            ret, frame = self.camera.read()

            if ret is True:
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
                # qt_image.scaled()
                scaled_img = qt_image.scaled(self.width, self.height)
                pix_map = QPixmap.fromImage(scaled_img)
                self.img_changed.emit(pix_map)

    def set_camera(self, camera):
        self.camera = camera

    def stop(self):
        self.running = False
        self.exit(0)
