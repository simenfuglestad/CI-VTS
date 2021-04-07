import cv2
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import time


class Camera(QThread):
    img_changed = Signal(bytes)
    got_frame = Signal(bytes)

    def __init__(self, width=420, height=640, res_width=1280.0, res_height=1024.0, running=True,
                 parent=None):
        super().__init__(parent)
        self.capture_indices = self.scan_capture_indices()
        self.capture_device = None

        self.res_width = res_width
        self.res_height = res_height
        self.current_frame = None
        self.running = running
        self.width = width
        self.height = height

        self.live = True
        self.recording = False
        self.out = None

        # self.mutex = QMutex()

        if len(self.capture_indices) > 0:
            self.set_capture_device(self.capture_indices[0])

    def run(self):
        while self.running and self.capture_device.isOpened():
            ret, frame = self.capture_device.read()
            # print(ret)
            if ret is True:
                # print(self.recording)
                h, w, ch = frame.shape
                if self.out is not None:
                    if self.recording:
                        # frame = cv2.flip(frame, 0)
                        if not type(frame) == str:
                            print("writing frame")
                            # self.mutex.lock()
                            print(self.out)
                            self.out.write(frame)
                            # self.mutex.unlock()

                elif self.live:
                    bytes_per_line = ch * w
                    qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    scaled_img = qt_image.scaled(self.width, self.height, Qt.KeepAspectRatio)
                    pix_map = QPixmap.fromImage(scaled_img)
                    self.img_changed.emit(pix_map)

        if self.capture_device.isOpened():
            self.capture_device.release()
        # print("cam thread reached end")

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
        self.recording = False
        time.sleep(1)
        if self.out is not None:
            if self.out.isOpened():
                print("releasing writer")
                # self.mutex.lock()
                self.out.release()
                # self.mutex.unlock()
        self.live = True

    def set_rec_mode(self):
        print(self.capture_device.get(3))
        print(self.capture_device.get(4))
        print(self.capture_device.get(5))
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        # fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        self.out = cv2.VideoWriter('test.avi', fourcc, 60, (int(self.res_width), int(self.res_height)), isColor=True)
        self.recording = True
        self.live = False

    def set_capture_device(self, cap_index):
        if self.capture_device is not None:
            self.capture_device.release()
        self.capture_device = cv2.VideoCapture(cap_index)
        self.capture_device.set(cv2.CAP_PROP_FPS, 60)
        self.capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.res_width))
        self.capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.res_height))

