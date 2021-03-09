from PySide6.QtWidgets import *
from UI.settings_dialog import Ui_Dialog


class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
