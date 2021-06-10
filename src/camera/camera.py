import cv2
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
import time


class Camera(QThread):
    """
    Provides camera control and operation functionality

    Attributes
    ----------
    img_changed_signal:
        Qt signal object, emits pixel map when frame is updated
    cam_connected_signal:
        Qt signal object, emits connected signal upon (un)successful connection to camera
    """
    img_changed_signal = Signal(bytes)
    cam_connected_signal = Signal(bytes)

    def __init__(self, video_path, fps=60, width=420, height=640, res_width=1280.0, res_height=1024.0, running=True):
        """
        Instantiate camera configuration values and scan for available capture devices on the system.
        :param video_path:
        :param fps:
        :param width:
        :param height:
        :param res_width:
        :param res_height:
        :param running:
        """
        super().__init__()
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
        """
        Run a camera feed in a thread separate from main program.
        :return: None
        """
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
        """
        Update video path held by camera, for verification when setting a video path elsewhere in the application
        :param path: str path to videos
        :param video_name: name of a video to be recorded in the path
        :return: None
        """
        try:
            if os.path.exists(path):
                self.video_path = path + video_name
                return True
            else:
                return False
        except IOError as e:
            return False

    def shutdown(self):
        """
        Set flag to indicate stopping the camera fee. Recommend only running this on complete shutdown of application.
        :return: None
        """
        self.is_alive = False

    def disconnect(self):
        """
        Disconnect current camera, blocking run() from entering video capture sequence
        :return: None
        """
        if self.capture_device is not None:
            if self.capture_device.isOpened():
                self.capture_device.release()
        if self.out is not None:
            self.out.release()
        self.emit_cam_status()
        self.capture_device_nr = -1

    def set_fps(self, fps):
        """
        Verify if camera is connected, then set capture fps.
        :param fps: int fps to use for capture device
        :return: None
        """
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
        """
        Provide thread safe locking of is_running
        NOTE: THIS BEHAVIOUR MIGHE BE INCORRECT, consider revising
        :param is_running: bool to set ir_running to
        :return: None
        """
        self.mutex.lock()
        self.running = is_running
        self.mutex.unlock()

    def stop_cam(self):
        """
        Stop the camera feed
        :return:
        """
        self.running = False
        self.cam_connected_signal.emit(True)

    def scan_capture_indices(self, captures_to_try=5):
        """
        Scan user system for connected capture devices. Because of the way openCV handles connections, we must manually
        specify how many attempts we want to make: No way to easily determine which capture index is the correct camera
        :param captures_to_try: int indicating how many capture indices to scan
        :return: list of indices where a frame capture was successfull
        """
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
        """
        Emits a bool to indicate the success of camera connection
        :return: bool connection success
        """
        if self.capture_device is None or not self.capture_device.isOpened():
            self.cam_connected_signal.emit(False)
        else:
            self.cam_connected_signal.emit(True)

    def set_live_mode(self):
        """
        Set camera to capture and show frames, but disable recording. Useful for "dry-runs" in an experiment
        :return: None
        """
        self.recording = False
        time.sleep(1)
        if self.out is not None:
            if self.out.isOpened():
                print("releasing writer")
                self.out.release()
        self.live = True
        print("wrote " + str(self.frames_written) + " frames")

    def set_rec_mode(self, frames_to_write=0):
        """
        Set camera to both capture frames and enable recording
        :param frames_to_write:
        :return: None
        """
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

        if self.video_path[-4:len(vid_path)] == ".avi":
            self.out = cv2.VideoWriter(vid_path, fourcc, self.fps, (int(self.res_width), int(self.res_height)), isColor=True)
            self.recording = True
            self.live = False

    def set_capture_device(self, cap_index):
        """
        Sets the current capture device/camera to get frames from
        :param cap_index: int index of capture device to set
        :return: None
        """
        if self.capture_device is not None:
            self.capture_device.release()
        self.capture_device = cv2.VideoCapture(cap_index)
        self.capture_device_nr = cap_index
        self.capture_device.set(cv2.CAP_PROP_FPS, self.fps)
        self.capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.res_width))
        self.capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.res_height))
        self.emit_cam_status()

