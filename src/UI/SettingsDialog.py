from UI.settings_dialog import Ui_Dialog
from camera.camera import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import time


class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, serial_interface, camera, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        s = time.perf_counter()
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
        self.combo_framerate.setCurrentText((str(self.camera.fps)))
        self.btn_disc_camera.clicked.connect(self.disconnect_camera)
        # self.combo_camera.currentIndexChanged.connect(self.set_live_camera)

        self.camera.img_changed_signal.connect(lambda x: self.update_live_cam_view(x))

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

    def show_camera_status(self, status):
        if status is True:
            self.label_camera_status.setText("Connected")
            self.label_camera_status.setStyleSheet("QLabel { color : green }")
        else:
            self.label_camera_status.setText("Not Connected")
            self.label_camera_status.setStyleSheet("QLabel { color : red }")

    def set_camera_fps(self, combo_fps_value):
        fps = int(self.combo_framerate.itemText(combo_fps_value))
        self.camera.set_fps(fps)

    def disconnect_camera(self):
        self.feed_stopped = True
        # self.feed_reached_end = False
        self.camera.set_running(False)
        # time.sleep(1)
        self.camera.disconnect()
        # self.camera.running = False
        self.label_live_video_feed.clear()

    def restart_live_camera(self):
        """
        Called when camera thread is done, used for safely switching cameras
        :return: None
        """
        if not self.feed_stopped:
            self.camera.running = True
            self.camera.start()

    def set_live_camera(self, index=0):
        index = self.combo_camera.currentIndex()
        if len(self.available_cameras) > 0:
            # self.disconnect_camera()
            if self.camera.running:
                print("cam running")
                self.camera.set_running(False)
                print(index)
                self.camera.set_capture_device(self.available_cameras[index])
                # self.feed_stopped = True
                self.camera.set_running(True)

            else:
                print("cam not running")
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

    def showEvent(self, event):
        pass

    def closeEvent(self, event):
        pass

    def update_live_cam_view(self, img_data):
        if self.feed_stopped:
            self.label_live_video_feed.clear()
        else:
            self.label_live_video_feed.setPixmap(img_data)

    def slide_adjust_led_live(self):
        slide_val = self.hslider_LED_live.value()
        self.spin_LED_live.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "sl")

    def spin_adjust_led_live(self):
        spin_val = self.spin_LED_live.value()
        self.hslider_LED_live.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "sl")

    def scan_serial(self):
        s = time.perf_counter()
        ports = self.serial_interface.scan_serial()
        print(time.perf_counter() - s)
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
        self.serial_interface.send_data(slide_val, "ir5")

    def slide_adjust_ir_left(self):
        slide_val = self.hslider_IR_left.value()
        self.spin_IR_left.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir6")

    def slide_adjust_ir_right(self):
        slide_val = self.hslider_IR_right.value()
        self.spin_IR_right.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir3")

    def spin_adjust_ir_bottom(self):
        spin_val = self.spin_IR_bottom.value()
        self.hslider_IR_bottom.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir5")

    def spin_adjust_ir_left(self):
        spin_val = self.spin_IR_left.value()
        self.hslider_IR_left.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir6")

    def spin_adjust_ir_right(self):
        spin_val = self.spin_IR_right.value()
        self.hslider_IR_right.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir3")

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


