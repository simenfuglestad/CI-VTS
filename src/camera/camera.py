import cv2
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
import time


class Camera(QThread):
    img_changed_signal = Signal(bytes)
    cam_connected_signal = Signal(bytes)

    def __init__(self, video_path, fps=60, width=420, height=640, res_width=1280.0, res_height=1024.0, running=True,
                 parent=None):
        super().__init__(parent)
        self.is_alive = True
        self.capture_device_nr = -1
        self.capture_device = None
        self.capture_indices = self.scan_capture_indices()
        self.camera_removed_flag = False

        self.res_width = res_width
        self.res_height = res_height
        self.fps = fps
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
                if self.capture_device.isOpened():
                    try:
                        ret, frame = self.capture_device.read()
                        if ret is True:
                            self.camera_removed_flag = False
                            h, w, ch = frame.shape
                            if self.out is not None:
                                if self.recording:
                                    self.out.write(frame)
                                    self.frames_written = self.frames_written + 1

                            bytes_per_line = ch * w
                            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                            scaled_img = qt_image.scaled(self.width, self.height, Qt.KeepAspectRatio)
                            pix_map = QPixmap.fromImage(scaled_img)
                            self.img_changed_signal.emit(pix_map)
                        else:
                            self.camera_removed_flag = True

                    except Exception as e:
                        self.set_running(False)
                        print("Excepting")
                        print(e)

    def set_video_path(self, path, video_name=""):
        try:
            if os.path.exists(path):
                self.video_path = path + video_name
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
        self.capture_device_nr = -1

    def set_fps(self, fps):
        if self.recording:
            print("Cannot set fps while recording")
            return False
        elif self.capture_device is None:
            print("Camera is not connected")
            return False
        elif not self.capture_device.isOpened():
            print("Camera is not open")
        else:
            self.fps = fps
            self.set_running(False)
            self.set_capture_device(self.capture_device_nr)
            self.set_running(True)
            return True

    def set_running(self, is_running):
        self.mutex.lock()
        self.running = is_running
        self.mutex.unlock()

    def stop_cam(self):
        self.running = False
        self.cam_connected_signal.emit(True)

    def scan_capture_indices(self, captures_to_try=5):
        indices = []
        for i in range(0, captures_to_try):
            if self.capture_device is not None:
                if i == self.capture_device_nr and not self.camera_removed_flag:
                    indices.append(i)
                    continue
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
                self.out.release()
        self.live = True
        print("wrote " + str(self.frames_written) + " frames")

    def set_rec_mode(self, frames_to_write=0):
        self.frames_written = 0
        print(self.capture_device.get(3))
        print(self.capture_device.get(4))
        print(self.capture_device.get(5))
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        vid_path = ""
        if os.path.isfile(self.video_path):
            print("recording with same name already exists")
            done = False
            index = 1
            [name, ext] = self.video_path.split('.')
            print(name)
            while not done:
                new_video_path = name + "(" + str(index) + ")." + ext
                if not os.path.isfile(new_video_path):
                    done = True
                    vid_path = new_video_path
                    # self.video_path = new_video_path
                else:
                    index = index + 1
        else:
            vid_path = self.video_path

        print(self.video_path)
        if self.video_path[-4:len(vid_path)] == ".avi":
            self.out = cv2.VideoWriter(vid_path, fourcc, self.fps, (int(self.res_width), int(self.res_height)), isColor=True)
            self.recording = True
            self.live = False

    def set_capture_device(self, cap_index):
        if self.capture_device is not None:
            self.capture_device.release()
        self.capture_device = cv2.VideoCapture(cap_index)
        self.capture_device_nr = cap_index
        self.capture_device.set(cv2.CAP_PROP_FPS, self.fps)
        self.capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.res_width))
        self.capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.res_height))
        self.emit_cam_status()

