
import sys
import cv2
from PySide6.QtWidgets import *

from UI.MainWindow import MainWindow
from serial_interface.serial_interface import *
from arduino.arduino import Arduino
from UI.AnalysisDialog import AnalysisDialog
from UI.SettingsDialog import SettingsDialog


class Main(QApplication):
    def __init__(self):
        super().__init__()
        # self.thread_pool = QThrea
        # init serial_interface interface
        self.serial_interface = SerialInterface()

        # Init Camera
        self.camera = cv2.VideoCapture(0)
        # self.camera.start()

        # init Arduino
        self.arduino = Arduino()

        # init UI
        self.settings_dialog = SettingsDialog(
            serial_interface=self.serial_interface,
            camera=self.camera)

        self.analysis_dialog = AnalysisDialog()

        self.main_window = MainWindow(
            settings_dialog=self.settings_dialog,
            analysis_dialog=self.analysis_dialog,
            serial_interface=self.serial_interface,
            size=self.primaryScreen().size())

        self.main_window.setWindowTitle("CI-VTS")
        self.main_window.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    app = Main()
    sys.exit(app.exec_())
