from PySide6.QtWidgets import *
from UI.settings_dialog import Ui_Dialog
from PySide6 import Qt


class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, serial_interface, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.device_name = None
        self.serial_interface = serial_interface
        self.populate_available_serial_devices()

        self.combo_serial.currentIndexChanged.connect(self.set_current_device)
        self.btn_verify_serial.clicked.connect(self.verify_serial_connection)

        self.hslider_IR_LED.valueChanged.connect(self.slide_adjust_ir)
        # self.hslider_IR_LED.sliderReleased.connect(self.slide_release_adjust_ir)
        self.hslider_IR_LED.sliderPressed.connect(self.slide_pressed_adjust_ir)

        self.spin_IR_LED.valueChanged.connect(self.spin_adjust_ir)

        self.btn_disc_serial.clicked.connect(self.disconnect_serial)

    def disconnect_serial(self):
        self.serial_interface.close_serial()

    def slide_adjust_ir(self):
        slide_val = self.hslider_IR_LED.value()
        self.spin_IR_LED.setValue(slide_val)
        # self.serial_interface.send_data(self.hslider_IR_LED.value())

    def spin_adjust_ir(self):
        spin_val = self.spin_IR_LED.value()
        self.hslider_IR_LED.setValue(spin_val)
        self.serial_interface.send_data(spin_val)

    def slide_release_adjust_ir(self):
        slider_val = self.hslider_IR_LED.value()
        self.spin_IR_LED.setValue(slider_val)
        self.serial_interface.send_data(slider_val)

    def slide_pressed_adjust_ir(self):
        slider_val = self.hslider_IR_LED.value()
        self.spin_IR_LED.setValue(slider_val)
        self.serial_interface.send_data(slider_val)

    def set_current_device(self):
        self.device_name = self.combo_serial.currentText()
        self.serial_interface.connect_serial(self.device_name)

    def populate_available_serial_devices(self):
        for i in self.serial_interface.serial_devices:
            self.combo_serial.addItem(i)

    def verify_serial_connection(self):
        if self.serial_interface.verify_current_connection():
            self.label_serial_status.setText("CONNECTION AVAILABLE")
        else:
            self.label_serial_status.setText("COULD NOT CONNECT")


