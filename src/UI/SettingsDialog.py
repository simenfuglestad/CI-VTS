from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from UI.settings_dialog import Ui_Dialog
import cv2
from camera.camera import CameraLiveFeed
import time

class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, serial_interface, camera, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.capture = camera
        self.capture.set(cv2.CAP_PROP_FPS, int(30))

        self.feed = CameraLiveFeed(
            camera=self.capture
            # width=self.label_live_video_feed.width(),
            # height=self.label_live_video_feed.height()
        )
        self.feed.img_changed.connect(lambda x: self.view_live_camera(x))

        self.device_name = None
        self.serial_interface = serial_interface
        self.scan_serial()
        self.connect_current_device()

        self.combo_serial.currentIndexChanged.connect(self.connect_current_device)
        # self.btn_verify_serial.clicked.connect(self.verify_serial_connection)

        self.hslider_IR_bottom.valueChanged.connect(self.slide_adjust_ir_bottom)
        self.hslider_IR_left.valueChanged.connect(self.slide_adjust_ir_left)
        self.hslider_IR_right.valueChanged.connect(self.slide_adjust_ir_right)

        self.spin_IR_bottom.valueChanged.connect(self.spin_adjust_ir_bottom)
        self.spin_IR_left.valueChanged.connect(self.spin_adjust_ir_left)
        self.spin_IR_right.valueChanged.connect(self.spin_adjust_ir_right)

        self.btn_disc_serial.clicked.connect(self.disconnect_serial)

        self.btn_scan_serial.clicked.connect(self.scan_serial)

        self.btn_connect_serial.clicked.connect(self.connect_current_device)

        self.hslider_LED_live.valueChanged.connect(self.slide_adjust_led_live)

    def showEvent(self, event):
        self.feed.start()

    def closeEvent(self, event):
        self.feed.stop()

    def view_live_camera(self, img_data):
        self.label_live_video_feed.setPixmap(img_data)
        self.label_live_video_feed.resize(600, 800)

    def slide_adjust_led_live(self):
        slide_val = self.hslider_LED_live.value()
        self.spin_LED_live.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "sl")

    def spin_adjust_led_live(self):
        spin_val = self.spin_LED_live.value()
        self.hslider_LED_live.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "sl")

    def scan_serial(self):
        ports = self.serial_interface.scan_serial()
        self.combo_serial.clear()
        for p in ports:
            self.combo_serial.addItem(p)

    def disconnect_serial(self):
        self.serial_interface.close_serial()
        self.verify_serial_connection()
        self.label_serial_status.setText("DISCONNECTED")

    def slide_adjust_ir_bottom(self):
        slide_val = self.hslider_IR_bottom.value()
        self.spin_IR_bottom.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir3")

    def slide_adjust_ir_left(self):
        slide_val = self.hslider_IR_left.value()
        self.spin_IR_left.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir5")

    def slide_adjust_ir_right(self):
        slide_val = self.hslider_IR_right.value()
        self.spin_IR_right.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir6")

    def spin_adjust_ir_bottom(self):
        spin_val = self.spin_IR_bottom.value()
        self.hslider_IR_bottom.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir3")

    def spin_adjust_ir_left(self):
        spin_val = self.spin_IR_left.value()
        self.hslider_IR_left.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir5")

    def spin_adjust_ir_right(self):
        spin_val = self.spin_IR_right.value()
        self.hslider_IR_right.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir6")

    def slide_release_adjust_ir(self):
        slider_val = self.hslider_IR_LED.value()
        self.spin_IR_LED.setValue(slider_val)
        self.serial_interface.send_data(slider_val, "ir")

    def slide_pressed_adjust_ir(self):
        slider_val = self.hslider_IR_LED.value()
        self.spin_IR_LED.setValue(slider_val)
        self.serial_interface.send_data(slider_val, "ir")

    def connect_current_device(self):
        self.device_name = self.combo_serial.currentText()
        self.serial_interface.connect_serial(self.device_name)
        self.verify_serial_connection()
        # self.label_serial_info.setText(str(self.serial_interface.serial_connection.get_settings()))

    def verify_serial_connection(self):
        if self.serial_interface.verify_current_connection():
            self.label_serial_status.setText("CONNECTION AVAILABLE")
        else:
            self.label_serial_status.setText("COULD NOT CONNECT")


