from PySide6.QtCore import *
from PySide6.QtWidgets import *
from UI.ui import Ui_MainWindow
from UI.AnalysisDialog import AnalysisDialog
from UI.SettingsDialog import SettingsDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, size, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.settings_dialog = SettingsDialog()
        QObject.connect(self.actionSetup, SIGNAL("triggered()"), self.settings_dialog.show)

        self.analysis_dialog = AnalysisDialog()
        QObject.connect(self.actionView, SIGNAL("triggered()"), self.analysis_dialog.show)

        self.resize(size.width(), size.height())

