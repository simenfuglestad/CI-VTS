from PySide6.QtCore import *
from PySide6.QtWidgets import *
# import settings_dialog
from UI import settings_dialog
from UI import ui


class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, size, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.dialog = QDialog()
        self.dialog.setMaximumSize(800, 600)
        self.settings_dialog = settings_dialog.Ui_Dialog().setupUi(self.dialog)

        QObject.connect(self.actionCamera, SIGNAL("triggered()"), self.dialog.show)

        self.resize(size.width(), size.height())