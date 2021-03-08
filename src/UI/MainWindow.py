from PySide6.QtCore import *
from PySide6.QtWidgets import *
# import settings_dialog
from UI import ui, settings_dialog


class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, size, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.dialog = QDialog()

        # self.dialog.setMaximumSize(size.width() / 2, size.height() / 2)
        self.settings_dialog = settings_dialog.Ui_Dialog().setupUi(self.dialog)
        self.dialog.resize(size.width() / 2, size.height() / 2)

        QObject.connect(self.actionSetup, SIGNAL("triggered()"), self.dialog.show)
        self.resize(size.width(), size.height())