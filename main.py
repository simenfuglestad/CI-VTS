from ui import Ui_MainWindow
import settings_dialog
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.dialog = QDialog()
        self.settings_dialog = settings_dialog.Ui_Dialog().setupUi(self.dialog)
        QObject.connect(self.actionCamera, SIGNAL("triggered()"), self.dialog.show)

        self.resize(1920, 1080)


if __name__ == '__main__':
    import sys
    from ui import Ui_MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())