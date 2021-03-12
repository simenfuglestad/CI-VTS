from PySide6.QtWidgets import *
from UI.settings_dialog import Ui_Dialog


class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, serial_interface, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.device_name = None
        self.serial_interface = serial_interface
        self.scan_serial()
        self.connect_current_device()

        self.combo_serial.currentIndexChanged.connect(self.connect_current_device)
        # self.btn_verify_serial.clicked.connect(self.verify_serial_connection)

        self.hslider_IR_LED.valueChanged.connect(self.slide_adjust_ir)
        # self.hslider_IR_LED.sliderReleased.connect(self.slide_release_adjust_ir)
        # self.hslider_IR_LED.sliderPressed.connect(self.slide_pressed_adjust_ir)

        self.spin_IR_LED.valueChanged.connect(self.spin_adjust_ir)

        self.btn_disc_serial.clicked.connect(self.disconnect_serial)

        self.btn_scan_serial.clicked.connect(self.scan_serial)

        self.btn_connect_serial.clicked.connect(self.connect_current_device)

        self.hslider_LED_live.valueChanged.connect(self.slide_adjust_led_live)

    def slide_adjust_led_live(self):
        slide_val = self.hslider_LED_live.value()
        self.spin_LED_live.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "st")

    def spin_adjust_led_live(self):
        spin_val = self.spin_LED_live.value()
        self.hslider_LED_live.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "st")

    def scan_serial(self):
        ports = self.serial_interface.scan_serial()
        self.combo_serial.clear()
        for p in ports:
            self.combo_serial.addItem(p)

    def disconnect_serial(self):
        self.serial_interface.close_serial()
        self.verify_serial_connection()
        self.label_serial_status.setText("DISCONNECTED")

    def slide_adjust_ir(self):
        slide_val = self.hslider_IR_LED.value()
        self.spin_IR_LED.setValue(slide_val)
        self.serial_interface.send_data(slide_val, "ir")

    def spin_adjust_ir(self):
        spin_val = self.spin_IR_LED.value()
        self.hslider_IR_LED.setValue(spin_val)
        self.serial_interface.send_data(spin_val, "ir")

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


