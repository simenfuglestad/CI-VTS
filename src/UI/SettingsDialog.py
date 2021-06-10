from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from UI.settings_dialog import Ui_Dialog
import cv2
from camera.camera import *
import time


class SettingsDialog(QDialog, Ui_Dialog):
    """
    User interface component allowing users configure the infrared LEDs, the camera, and the Arduino.
    Also provides a real-time camera feed.
    """
    def __init__(self, serial_interface, camera):
        """
        Bind all UI components to their respective buttons and
        :param serial_interface: instance of serial_interface.py, serve as connection with Arduino
        :param camera: instance of camera.py, serves as camera control
        """
        super().__init__()
        self.setupUi(self)
        self.camera = camera
        self.feed_stopped = False
        self.camera.cam_connected_signal.connect(self.show_camera_status)
        self.camera.finished.connect(self.restart_live_camera)
        self.available_cameras = []
        self.get_available_cameras()
        self.btn_connect_camera.clicked.connect(self.set_live_camera)
        self.btn_scan_camera.clicked.connect(self.get_available_cameras)
        self.combo_camera.activated.connect(lambda x: self.set_live_camera(x))
        self.combo_framerate.activated.connect(lambda x: self.set_camera_fps(x))
        self.btn_disc_camera.clicked.connect(self.disconnect_camera)

        self.camera.img_changed_signal.connect(lambda x: self.update_live_cam_view(x))

        self.device_name = None
        self.serial_interface = serial_interface
        self.scan_serial()

        self.connect_current_device()

        self.combo_serial.currentIndexChanged.connect(self.connect_current_device)

        self.hslider_IR_bottom.valueChanged.connect(self.slide_adjust_ir_bottom)
        self.hslider_IR_left.valueChanged.connect(self.slide_adjust_ir_left)
        self.hslider_IR_right.valueChanged.connect(self.slide_adjust_ir_right)

        self.spin_IR_bottom.valueChanged.connect(self.spin_adjust_ir_bottom)
        self.spin_IR_left.valueChanged.connect(self.spin_adjust_ir_left)
        self.spin_IR_right.valueChanged.connect(self.spin_adjust_ir_right)

        self.btn_disc_serial.clicked.connect(self.disconnect_serial)

        self.btn_scan_serial.clicked.connect(self.scan_serial)

        self.btn_connect_serial.clicked.connect(self.connect_current_device)

        self.buttonBox.accepted.connect(self.close)
        self.buttonBox.rejected.connect(self.close)

    def show_camera_status(self, status):
        """
        Update label showing if a camera is connected or not
        :param status: bool=true if camera is connected
        :return: None
        """
        if status is True:
            self.label_camera_status.setText("Connected")
            self.label_camera_status.setStyleSheet("QLabel { color : green }")
        else:
            self.label_camera_status.setText("Not Connected")
            self.label_camera_status.setStyleSheet("QLabel { color : red }")

    def set_camera_fps(self, combo_fps_value):
        """
        Get fps value from combobox and attempt to set camera fps
        :param combo_fps_value:
        :return: None
        """
        fps = int(self.combo_framerate.itemText(combo_fps_value))
        self.camera.set_fps(fps)

    def disconnect_camera(self):
        """
        Stop video feed and attempt to disconnect camera
        :return:
        """
        self.feed_stopped = True
        self.camera.set_running(False)
        self.camera.disconnect()
        self.label_live_video_feed.clear()

    def restart_live_camera(self):
        """
        Called when camera thread is done, used for safely switching cameras
        :return: None
        """
        if not self.feed_stopped:
            self.camera.running = True
            self.camera.start()

    def set_live_camera(self):
        """
        Selects a camera for the live feed, same camera will be used for recoding experiments
        :return: None
        """
        index = self.combo_camera.currentIndex()
        if len(self.available_cameras) > 0:
            if self.camera.running:
                self.camera.set_running(False)
                self.camera.set_capture_device(self.available_cameras[index])
                self.camera.set_running(True)

            else:
                self.camera.set_capture_device(self.available_cameras[index])
                self.feed_stopped = False
                self.camera.set_running(True)
        else:
            print("no cameras")

    def get_available_cameras(self):
        """
        :return: list of capture devices with indexes corresponding to indexes in combobox
        """
        indices = self.camera.scan_capture_indices()
        current_cam_index = self.combo_camera.currentIndex()
        self.combo_camera.clear()
        if len(indices) == 0:
            self.combo_camera.addItem("No cameras available")
        else:
            for i in indices:
                self.combo_camera.addItem("Camera " + str(i + 1))
            self.combo_camera.setCurrentIndex(current_cam_index)
        self.available_cameras = indices
        return indices

    def update_live_cam_view(self, img_data):
        """
        Sets the live feed label to show newest frame
        :param img_data: QPixelMap of newest frame
        :return: None
        """
        if self.feed_stopped:
            self.label_live_video_feed.clear()
        else:
            self.label_live_video_feed.setPixmap(img_data)

    def scan_serial(self):
        """
        Get available serial devices from serial_interface.py and display them in combobox
        :return: None
        """
        ports = self.serial_interface.scan_serial()
        self.combo_serial.clear()
        for p in ports:
            self.combo_serial.addItem(p)

    def disconnect_serial(self):
        """
        Use serial interface to disconnect and set labels indicating disconnection
        :return:
        """
        self.serial_interface.close_serial()
        self.verify_serial_connection()
        self.label_serial_status.setText("DISCONNECTED")

    def slide_adjust_ir_bottom(self):
        """
        Event fired when adjusting slider 'IR Bottom'
        :return: None
        """
        slide_val = self.hslider_IR_bottom.value()
        self.spin_IR_bottom.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir6")

    def slide_adjust_ir_left(self):
        """
        Event fired when adjusting slider 'IR Left'
        :return: None
        """
        slide_val = self.hslider_IR_left.value()
        self.spin_IR_left.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir3")

    def slide_adjust_ir_right(self):
        """
        Event fired when adjusting slider 'IR Right'
        :return: None
        """
        slide_val = self.hslider_IR_right.value()
        self.spin_IR_right.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir5")

    def spin_adjust_ir_bottom(self):
        """
        Event fired when adjusting slider 'IR Bottom'
        :return: None
        """
        spin_val = self.spin_IR_bottom.value()
        self.hslider_IR_bottom.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir6")

    def spin_adjust_ir_left(self):
        """
        Event fired when adjusting spinbox 'IR Left'
        :return: None
        """
        spin_val = self.spin_IR_left.value()
        self.hslider_IR_left.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir3")

    def spin_adjust_ir_right(self):
        """
        Event fired when adjusting spinbox 'IR Right'
        :return: None
        """
        spin_val = self.spin_IR_right.value()
        self.hslider_IR_right.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir5")

    def connect_current_device(self):
        """
        Pass a device name to serial_interface.py and attept to connect
        :return: None
        """
        self.device_name = self.combo_serial.currentText()
        self.serial_interface.connect_serial(self.device_name)
        self.verify_serial_connection()

    def verify_serial_connection(self):
        """
        Use serial interface to display connection status
        :return:
        """
        if self.serial_interface.verify_current_connection():
            self.label_serial_status.setText("CONNECTION AVAILABLE")
        else:
            self.label_serial_status.setText("COULD NOT CONNECT")
