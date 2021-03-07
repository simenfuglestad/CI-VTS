from UI.MainWindow import MainWindow
from PySide6.QtWidgets import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    window = MainWindow(size=screen.size())
    window.setWindowTitle("CI-VTS")
    window.show()
    sys.exit(app.exec_())
