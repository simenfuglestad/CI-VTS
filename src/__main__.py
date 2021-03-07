import sys

from PySide6.QtWidgets import *

from UI.MainWindow import MainWindow
from serial.serial_interface import *
from stimulus.stimulus import Stimulus
from arduino.arduino import Arduino


class Main(QApplication):
    def __init__(self):
        super().__init__()

        #init serial interface
        self.serial = SerialInterface()

        #init stimulus
        self.stimulus = Stimulus()

        #init Arduino
        self.arduino = Arduino()

        #init UI
        self.window = MainWindow(size=self.primaryScreen().size())
        self.window.setWindowTitle("CI-VTS")
        self.window.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    app = Main()
    sys.exit(app.exec_())
