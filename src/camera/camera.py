import cv2
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import time


class Camera(QThread):
    img_changed_signal = Signal(bytes)
    cam_connected_signal = Signal(bytes)

    def __init__(self, video_path, width=420, height=640, res_width=1280.0, res_height=1024.0, running=True,
                 parent=None):
        super().__init__(parent)
        self.is_alive = True
        self.capture_indices = self.scan_capture_indices()
        self.capture_device = None
        self.capture_device_nr = -1

        self.res_width = res_width
        self.res_height = res_height
        self.current_frame = None
        self.running = running
        self.width = width
        self.height = height

        self.live = True
        self.recording = False
        self.out = None

        self.video_path = video_path

        self.mutex = QMutex()

        self.frames_written = 0

        if len(self.capture_indices) > 0:
            self.set_capture_device(self.capture_indices[0])
            print(self.capture_device)

    def run(self):
        while self.is_alive:
            if self.running and self.capture_device is not None:
                # print("camera is running")
                if self.capture_device.isOpened():
                    try:
                        ret, frame = self.capture_device.read()
                        if ret is True:
                            # print(self.recording)
                            h, w, ch = frame.shape
                            if self.out is not None:
                                if self.recording:
                                    # print("writing frame")
                                    # self.mutex.lock()
                                    self.out.write(frame)
                                    self.frames_written = self.frames_written + 1
                                    # self.mutex.unlock()

                            bytes_per_line = ch * w
                            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                            scaled_img = qt_image.scaled(self.width, self.height, Qt.KeepAspectRatio)
                            pix_map = QPixmap.fromImage(scaled_img)
                            self.img_changed_signal.emit(pix_map)

                    except Exception as e:
                        self.set_running(False)
                        print(e)

        if self.capture_device.isOpened():
            self.capture_device.release()
        print("cam thread reached end")

    def set_video_path(self, path):
        try:
            if os.path.exists(path):
                self.video_path = path
                return True
            else:
                return False
        except IOError as e:
            return False

    def shutdown(self):
        self.is_alive = False

    def disconnect(self):
        if self.capture_device is not None:
            if self.capture_device.isOpened():
                self.capture_device.release()
        if self.out is not None:
            self.out.release()
        self.emit_cam_status()

    def set_running(self, is_running):
        # print(self.mutex.)
        self.mutex.lock()
        self.running = is_running
        self.mutex.unlock()
        # time.sleep(0.5)

    def stop_cam(self):
        self.running = False
        self.cam_connected_signal.emit(True)

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

    def emit_cam_status(self):
        if self.capture_device is None or not self.capture_device.isOpened():
            self.cam_connected_signal.emit(False)
        else:
            self.cam_connected_signal.emit(True)

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
        print("wrote " + str(self.frames_written) + " frames")

    def set_rec_mode(self):
        self.frames_written = 0
        print(self.capture_device.get(3))
        print(self.capture_device.get(4))
        print(self.capture_device.get(5))
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.out = cv2.VideoWriter(self.video_path + "test.avi", fourcc, 60, (int(self.res_width), int(self.res_height)), isColor=True)
        self.recording = True
        self.live = False

    def set_capture_device(self, cap_index):
        if self.capture_device is not None:
            self.capture_device.release()
        self.capture_device = cv2.VideoCapture(cap_index)
        self.capture_device_nr = cap_index
        self.capture_device.set(cv2.CAP_PROP_FPS, 60)
        self.capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.res_width))
        self.capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.res_height))
        self.emit_cam_status()

