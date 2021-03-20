import cv2
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import time

class CameraLiveFeed(QThread):
    img_changed = Signal(bytes)

    def __init__(self, camera, parent=None):
        super().__init__(parent)
        self.cap = camera
        self.current_frame = None
        self.running = False

    def run(self):
        while True:
            time.sleep(0.05)
            ret, frame = self.cap.read()
            # image = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            # h, w, ch = image.shape
            # bytesPerLine = ch * w
            # qt_image = QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)
            # # p = qt_image.scaled()
            self.send_img(frame)
            key = cv2.waitKey(20)
            if key == 27:
                break
        print("feed done")

    def send_img(self, frame):
        self.img_changed.emit(frame)

def init_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("skhbfgd")
        return
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    ret, frame = cap.read()
    print(frame)
    cv2.imshow('view', frame)
    print(cap)
    print("init camera")

    while ret:
        key = cv2.waitKey(20)
        if key == 27:
            break
    cv2.destroyWindow('view')